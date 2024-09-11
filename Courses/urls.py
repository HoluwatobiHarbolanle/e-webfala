from django.urls import include, path
from .views import instructor_dashboard
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet

router = DefaultRouter()

router.register(r"", CourseViewSet)

urlpatterns = [
    path("instructor_dashboard", instructor_dashboard, name="instructor_dashboard"),
    path("", include(router.urls)),
]
