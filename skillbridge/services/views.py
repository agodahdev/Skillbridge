from django.shortcuts import render, redirect, get_object_or_404
from .forms import SkillServiceForm, BookingRequestForm
from django.contrib.auth.decorators import login_required
from .models import SkillService, BookingRequest
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseForbidden
from django.contrib import messages 


# This view allows a logged-in user (provider) to submit a service
@login_required
def submit_service(request):
    if request.method == 'POST':
        form = SkillServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.provider = request.user  # set the current user as provider
            service.is_approved = False  # Admin must approve before showing
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
    """Show the homepage."""
    return render(request, 'home.html')


@login_required
def book_service(request, service_id):
    """
    Let logged-in users book a service.
    Gets the service by ID and creates a booking if form is valid.
    """
    service = get_object_or_404(SkillService, id=service_id, is_approved=True)

    if request.method == 'POST':
        form = BookingRequestForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.client = request.user
            booking.service = service
            booking.save()
            messages.success(request, "Your booking request has been sent.")
            return redirect('dashboard')  # or a "booking success" page
        else:
            print("❌ Booking form errors:", form.errors)
    else:
        form = BookingRequestForm()
    return render(request, 'services/book_service.html',
                  {'form': form, 'service': service})


def submission_success(request):
    """Show success page after submitting a service."""
    return render(request, 'services/submission_success.html')


def signup(request):
    """
    Handle new user registration.
    Creates account and logs them in automatically.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in after signup
        return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def dashboard(request):
    """
    Show user's dashboard with three tabs:
    - My Services (services I created)
    - My Bookings (services I booked)
    - Client Requests (bookings on my services)
    """

    my_services = SkillService.objects.filter(provider=request.user)
    my_client_bookings = BookingRequest.objects.filter(client=request.user)
    incoming_bookings = BookingRequest.objects.filter(service__provider=request.user)

    return render(request, 'services/dashboard.html', {
        'my_services': my_services,
        'my_bookings': my_client_bookings,
        'bookings_on_my_services': incoming_bookings,
    })


# view to edit an existing service
@login_required
def edit_service(request, service_id):
    """
    Let users edit their own services.
    Shows error if they try to edit someone else's service.
    """
    service = get_object_or_404(SkillService, id=service_id)

    # Check if user owns this service
    if service.provider != request.user:
        return HttpResponseForbidden("You cannot edit this service.")

    if request.method == 'POST':

        form = SkillServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()  # Save updates to the database
            messages.success(request, "Your service was updated successfully.")
            return redirect('dashboard')  # Go back to the dashboard

    else:
        form = SkillServiceForm(instance=service)

    return render(request, 'services/edit_service.html',
                  {'form': form, 'service':service})


# View to delete service
@login_required
def delete_service(request, service_id): 
    """
    Let users delete their own services.
    Only works if you're the owner of the service.
    """
    service = get_object_or_404(SkillService, id=service_id)

    # Check if user owns this service
    if service.provider != request.user:
        return HttpResponseForbidden("You cannot delete this service.")

    if request.method == 'POST':
        service.delete() 
        messages.success(request, "Service deleted successfully.") 
        return redirect('dashboard')

    return render(request, 'services/delete_service.html',  
                  {'service': service})

@login_required
def manage_bookings(request):
    """
    Show providers all bookings on their services.
    They can update the status (pending/accepted/rejected).
    """
    bookings = BookingRequest.objects.filter(service__provider=request.user)

    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        new_status = request.POST.get('status')

        booking = get_object_or_404(BookingRequest, id=booking_id, service__provider=request.user)
        booking.status = new_status
        booking.save()
        return redirect('manage_bookings')

    return render(request, 'services/manage_bookings.html', {'bookings':bookings})


@login_required
def cancel_booking(request, pk):
    """
    Cancel a booking.
    Either the client or the provider can cancel.
    """
    booking = get_object_or_404(BookingRequest, pk=pk)

# Onkly client who made the booking or the provider of the service can cancel
    if request.user != booking.client and request.user != booking.service.provider:
        messages.error(request, "You don't have permission to cancel this booking.")
        return redirect('dashboard')

    if request.method == 'POST':
        booking.delete()
        messages.success(request, "Booking was cancelled.")
        return redirect('dashboard')

    messages.error(request, "Invalid request method.")
    return redirect('dashboard')
