# Generated by Django 4.1.4 on 2023-02-17 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meddata', '0008_profile_date_of_birth_profile_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='photo',
        ),
    ]
