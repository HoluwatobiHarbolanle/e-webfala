from django.urls import include, path
from .views import instructor_dashboard
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, CategoryViewSet, CategoryListView, CourseListView

# from .views import CourseViewSet, CourseListView
# from .views import CourseListView, CourseViewSet

router = DefaultRouter()

router.register(r"courses", CourseViewSet)
router.register(r"categories", CategoryViewSet)

urlpatterns = [
    path("instructor_dashboard", instructor_dashboard, name="instructor_dashboard"),
    path("categories", CategoryListView.as_view(template_name = "categories.html"), name = 'category_list'),
    path("api/", include(router.urls)),
    path("api/courses/", include(router.urls)),
    path("courses/", CourseListView.as_view(), name="course_list"),
]

