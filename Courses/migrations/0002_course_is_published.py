# Generated by Django 5.1.1 on 2024-09-11 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]