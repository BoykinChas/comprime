from django.db import models
from django.contrib.auth.models import User 
from django.db.models.signals import post_save 


# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
    
class child(models.Model):
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)
        profile = models.ForeignKey(User, on_delete=models.CASCADE)

    
# Create Profile When New User Signs up
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)