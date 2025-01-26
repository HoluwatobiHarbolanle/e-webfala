# Generated by Django 5.1.1 on 2024-09-18 12:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_profile'),
        ('Courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(upload_to='profile_image')),
                ('full_name', models.CharField(blank=True, max_length=100, null=True)),
                ('bio', models.CharField(blank=True, max_length=255, null=True)),
                ('courses_registered', models.ManyToManyField(to='Courses.course')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
