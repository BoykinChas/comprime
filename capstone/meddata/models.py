from django.db import models
from django.conf import settings
from django.contrib.auth.models import User 
from django.db.models.signals import post_save 


# Create your models here.


class Doctor(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField('Specalist/Dr', max_length=120)
    clinic = models.CharField('Clinic', max_length=120, null=True)
    address = models.CharField('Address', max_length=300)
    zip_code = models.CharField('Zip Code', max_length=15)
    phone = models.CharField('Contact Phone', max_length=25, blank=True)
    specialty = models.CharField('Specality', max_length=120)

    def __str__(self):
      return str(self.user)

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
      return str(self.user)
    
# Create Profile When New User Signs up
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)

