
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from .models import UserProfile
from django.contrib.auth.views import PasswordResetView
from dj_rest_auth.views import LogoutView

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
def profile_form(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = UserProfile(user = request.user)
        
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=profile)
    return render(request, "profile_form.html", {"form": form, "user_profile_type": "student"})


def view_profile(request):
    user = request.user
    profile = UserProfile.objects.all()
    return render(request, 'userprofile.html', {profile: 'profile'})
    

# login_required
# def profile_view(request):
#     profile = UserProfile.objects.get(user=request.user)

#     if request.method == 'POST':
#         form = UserProfileForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')  
#     else:
#         form = UserProfileForm(instance=profile)

#     return render(request, 'profile_form.html', {'form': form, 'profile': profile})



