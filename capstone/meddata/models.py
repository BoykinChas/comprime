from django.db import models
from django.contrib.auth.models import User 
from django.db.models.signals import post_save 


# Create your models here.
class Child(models.Model):
    name = models.CharField('Childs Name', max_length=120)
    dob = models.DateTimeField('Date of Birth')


class Doctor(models.Model):
    name = models.CharField('Specalist/Dr', max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip Code', max_length=15)
    phone = models.CharField('Contact Phone', max_length=25, blank=True)
    specialty = models.CharField('Specality', max_length=120)
    # clinic = models.CharField('Clinic', max_length=120)

    def __str__(self):
      return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    
# Create Profile When New User Signs up
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)