# Generated by Django 5.1.1 on 2024-09-11 11:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('category', models.CharField(blank=True, max_length=255)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cover_video', models.FileField(blank=True, null=True, upload_to='course_videos/')),
                ('cover_photo', models.ImageField(blank=True, null=True, upload_to='course_covers/')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('video_file', models.FileField(blank=True, null=True, upload_to='lessons/videos/')),
                ('pdf_file', models.FileField(blank=True, null=True, upload_to='lessons/pdfs/')),
                ('content', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='Courses.course')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('video_file', models.FileField(upload_to='videos/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='Courses.course')),
            ],
        ),
    ]
