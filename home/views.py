from django.shortcuts import render
from Courses.models import Course

# Create your views here.


def home(request):
    courses = Course.objects.all()
    return render(request, "home.html", {"courses": courses})
