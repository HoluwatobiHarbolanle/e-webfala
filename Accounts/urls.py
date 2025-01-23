from django.urls import path
from . import views

urlpatterns = [
    path('profile_form/', views.profile_form, name ="profile_form"),
]
