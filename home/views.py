from django.shortcuts import render
from Courses.models import Course

from django.contrib.auth import get_user_model
from django.http import HttpResponse

# Create your views here.


def home(request):
    courses = Course.objects.all()
    return render(request, "home.html", {"courses": courses})


def create_admin(request):
    User = get_user_model()
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser('admin', 'aishatmurtadho@gmail.com', 'Abdulwaahid@1963')
        return HttpResponse("Superuser created!")
    return HttpResponse("Admin already exists.")