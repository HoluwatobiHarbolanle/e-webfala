from django import forms
from .models import Course,Video,Lesson

class CourseTitleForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'cover_photo']

class CourseCategoryForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['category']

class CoursePriceForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['price']

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'video_file']

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'video_file', 'pdf_file', 'content']
