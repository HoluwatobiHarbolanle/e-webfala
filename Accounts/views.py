
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, InstructorProfileForm
from .models import UserProfile, InstructorProfile
from django.views import View
from django.contrib.auth.views import PasswordResetView
from dj_rest_auth.views import LogoutView
from django.conf import settings
import os

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


class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        """Handle GET request for logout to serve HTML."""
        if request.user.is_authenticated:
            self.logout(request)
        return render(request, "account/logout.html")


class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset.html'
    email_template_name = 'registration/password_reset_email.txt'
    html_email_template_name = 'registration/password_reset_email.html'
    
    
@login_required
def user_profile_form(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = UserProfile(user = request.user)
        
    if request.method == 'POST':
        if 'profile_pic' in request.FILES:
            if profile.profile_pic:
                old_picture_path = os.path.join(settings.MEDIA_ROOT, str(profile.profile_pic))
                if os.path.isfile(old_picture_path):
                    os.remove(old_picture_path)

        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=profile)
    return render(request, "user_profile_form.html", {"form": form})


class InstructorProfileView(View): 


    def get(self, request, step=1):
        # Initialize forms based on the step
        if step == 1:
            form = UserProfileForm(instance=request.user.userprofile)
        elif step == 2:
            instructor_profile, created = InstructorProfile.objects.get_or_create(user=request.user)
            form = InstructorProfileForm(instance=instructor_profile)
        else:
            return redirect('profile_complete')

        return render(request, 'profile/multi_step_form.html', {
            'form': form,
            'step': step,
        })
    def post(self, request, step=1):
        # Handle form submissions based on the step
        if step == 1:
            form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
            if form.is_valid():
                form.save()
                return redirect('multi_step_form', step=2)
        elif step == 2:
            instructor_profile = InstructorProfile.objects.get(user=request.user)
            form = InstructorProfileForm(request.POST, instance=instructor_profile)
            if form.is_valid():
                form.save()
                return redirect('profile_complete')

        # Re-render the same template with errors if form is invalid
        return render(request, 'profile/multi_step_form.html', {
            'form': form,
            'step': step,
        })

def view_user_profile(request):
    try:
        profile = UserProfile.objects.get(user=request.user)  # Get profile for the current user
    except UserProfile.DoesNotExist:
        profile = None  # Handle case where profile doesn't exist

    return render(request, 'userprofile.html', {'profile': profile})
    




