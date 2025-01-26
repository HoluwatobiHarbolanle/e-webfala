from django.contrib import admin
<<<<<<< HEAD
from .models import CustomUser
=======
from .models import CustomUser, UserProfile
>>>>>>> 841eeeea387a928f1446e8cbf39a8bf08abe4b11

# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("email", "username", "is_student", "is_instructor", "date_joined")


admin.site.register(CustomUser, CustomUserAdmin)
<<<<<<< HEAD
=======

admin.site.register(UserProfile)
>>>>>>> 841eeeea387a928f1446e8cbf39a8bf08abe4b11
