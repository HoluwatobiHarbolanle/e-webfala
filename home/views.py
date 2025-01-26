from django.shortcuts import render
<<<<<<< HEAD
from Courses.models import Course
=======
>>>>>>> 841eeeea387a928f1446e8cbf39a8bf08abe4b11

# Create your views here.


def home(request):
<<<<<<< HEAD
    courses = Course.objects.all()
=======
    courses = [
        {
            "id": 1,
            "title": "Web Development Masterclass",
            "description": "Learn to build modern, responsive websites...",
            "price": 4400,
            "image_url": "https://placehold.co/400x225",
        },
        {
            "id": 2,
            "title": "Backend Development Bootcamp",
            "description": "Dive deep into server-side development...",
            "price": 5500,
            "image_url": "https://placehold.co/400x225",
        },
        {
            "id": 3,
            "title": "Frontend Development Bootcamp",
            "description": "Learn to build modern, responsive websites...",
            "price": 4400,
            "image_url": "https://placehold.co/400x225",
        },
    ]
>>>>>>> 841eeeea387a928f1446e8cbf39a8bf08abe4b11
    return render(request, "home.html", {"courses": courses})
