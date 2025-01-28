from django import forms
from .models import UserProfile, InstructorProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_pic', 'first_name', 'last_name', 'bio'] 
        
class InstructorProfileForm(forms.ModelForm):
    class Meta:
        model = InstructorProfile
        fields = '__all__'