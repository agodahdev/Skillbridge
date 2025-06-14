from django.shortcuts import render, redirect
from .forms import SkillServiceForm, BookingRequestForm
from django.contrib.auth.decorators import login_required
from .models import SkillService, BookingRequest
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages


# This view allows a logged-in user (provider) to submit a service 
# @login required
def submit_service(request):
    if request.method == 'POST':
        form = SkillServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.provider = request.user #lset the current user as provider
            service.is_approved = False # Admin must approve before showing
            service.save()
            return redirect('submission_success')
    else:
        form = SkillServiceForm()
    return render(request, 'services/submit_service.html', {'form': form})

# Public view to Show all approved services
def service_list(request):
    query = request.GET.get('q')
    category = request.GET.get('category')
    services = SkillService.objects.filter(is_approved=True)

    if query:
        services = services.filter(title__icontains=query)

    if category and category != 'All':
        services = services.filter(category=category)
    
    return render(request, 'services/service_list.html', {
        'services': services,
        'query': query or '',
        'category': category or 'All'

    })

# Home page view
def home(request):
    return render(request, 'home.html')

def book_service(request, service_id):
    service = SkillService.objects.get(id=service_id)
    if request.method == 'POST':
        form = BookingRequestForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.client = request.user
            booking.service = service
            booking.save()
            return redirect('service_list') # or a "booking success" page
    else:
        form = BookingRequestForm()
    return render(request, 'services/book_service.html', {'form': form, 'service': service})

def submission_success(request):
    return render(request, 'services/submission_success.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
           user = form.save()
           login(request, user) #log in after signup
           return redirect('/')
    
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# @login_required
def dashboard(request):
    my_services = SkillService.objects.filter(provider=request.user)
    my_bookings = BookingRequest.objects.filter(client=request.user)
    bookings_on_my_services = BookingRequest.objects.filter(service__provider=request.user)

    return render(request, 'services/dashboard.html', {
        'my_services': my_services,
        'my_bookings': my_bookings,
        'bookings_on_my_services': bookings_on_my_services,
    })

# view to edit an existing service
# @login_required - only logged-in users can access this
def edit_service(request, service_id):
    service = get_object_or_404(SkillService, id=service_id)

    if service.provider != request.user: 
        return HttpResponseForbidden("You cannot edit this service.")

    if request.method == 'POST':
        
        form = SkillServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save() #Save updates to the database
            messages.success(request, "Your service was update successfully.")
            return redirect('dashboard') # Go back to the dashboard
    
    else: 
        form = SkillServiceForm(instance=service)

    return render (request, 'services/edit_service.html', {'form': form, 'service':service})


# View to delete service
#@ login_required
def delete_service(request, service_id):
    service = get_object_or_404(SkillService, id=service_id)

    if service.provider != request.user:
        return HttpResponseForbidden("You cannot delete this service.")

    if request.method == 'POST':
        service.delete() # Remove service from database
        messages.success(request, "Service deleted successfully.")
        return redirect('dashboard') # Back to dashboard after deletion

    
    return render(request, 'services/delete_service.html', {'service': service})
    
    