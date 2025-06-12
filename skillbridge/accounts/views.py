from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') #Redirect to login after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def submission_success(request):
    return render(request, 'services/submission_success.html')