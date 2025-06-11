from django.shortcuts import render, redirect
from .forms import SkillServiceForm
from django.contrib.auth.decorators import login_required
from .models import SkillService 

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
    services = SkillService.objects.filter(is_approved=True).order_by('-created_at')
    return render(request, 'services/service_list.html', {'services': services})

# Home page view
def home(request):
    return render(request, 'home.html')