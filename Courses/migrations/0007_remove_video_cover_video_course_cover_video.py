# Generated by Django 5.0.7 on 2024-09-10 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0006_video_cover_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='cover_video',
        ),
        migrations.AddField(
            model_name='course',
            name='cover_video',
            field=models.FileField(blank=True, null=True, upload_to='course_videos/'),
        ),
    ]