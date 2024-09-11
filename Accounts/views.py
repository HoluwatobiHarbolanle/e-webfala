from django.shortcuts import render

# Create your views here.

# from django.shortcuts import redirect
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.views import LoginView

# class CustomLoginView(LoginView):
#     def form_valid(self, form):
#         user = form.get_user()
#         if user.role == 'USER':
#             return redirect('user_home')  # Redirect to user-specific home page
#         elif user.role == 'INSTRUCTOR':
#             return redirect('instructor_home')  # Redirect to instructor-specific home page
#         return super().form_valid(form)

# def register_user(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST, request.FILES)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             login(request, user)
#             return redirect('home')  # Redirect to a success page
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'register_user.html', {'form': form})

# def register_instructor(request):
#     if request.method == 'POST':
#         form = InstructorRegistrationForm(request.POST)
#         if form.is_valid():
#             instructor = form.save(commit=False)
#             instructor.set_password(form.cleaned_data['password'])
#             instructor.save()
#             login(request, instructor)
#             return redirect('home')  # Redirect to a success page
#     else:
#         form = InstructorRegistrationForm()
#     return render(request, 'register_instructor.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserLoginForm, InstructorLoginForm

def user_login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('user_home')  # Redirect to a user home page or dashboard
    else:
        form = UserLoginForm(request)
    return render(request, 'user_login.html', {'form': form})

def instructor_login_view(request):
    if request.method == 'POST':
        form = InstructorLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('instructor_home')  # Redirect to an instructor home page or dashboard
    else:
        form = InstructorLoginForm(request)
    return render(request, 'instructor_login.html', {'form': form})