
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm


# Create your views here.
def custom_login_view(request):
    error_message = None
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            error_message = 'Invalid email or password'

    return render(request, 'accounts/login.html', {'error_message': error_message})


@login_required
def profile_view(request):
    profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'profile.html', {'form': form, 'profile': profile})
