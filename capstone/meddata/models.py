from django.db import models
from django.conf import settings
from django.contrib.auth.models import User 
from django.db.models.signals import post_save 

# Create your models here.

class Notes(models.Model):
   title = models.CharField(max_length=50)
   author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
   body = models.TextField()
   
   def __str__(self):
       return self.title + ' | ' + str(self.author)


YN_CHOICES=[
   ('yes', 'Yes'),
   ('not sure', 'Not Sure'),
   ('not yet', 'Not Yet'),
]

class Milestone(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    calms = models.CharField('Calms down when spoken to or picked up', max_length=10, choices=YN_CHOICES, null=True)
    looks = models.CharField('Looks at your face', max_length=10, choices=YN_CHOICES, null=True)
    happy = models.CharField('Seems happy to see you when you walk up', max_length=10, choices=YN_CHOICES, null=True)
    smiles = models.CharField('Smiles when you talk or smile to them', max_length=10, choices=YN_CHOICES, null=True)
    sounds = models.CharField('Makes sounds other than crying', max_length=10, choices=YN_CHOICES, null=True)
    loud = models.CharField('Reacts to loud sounds', max_length=10, choices=YN_CHOICES, null=True)
    watches = models.CharField('Watches you as you move', max_length=10, choices=YN_CHOICES, null=True)
    toy = models.CharField('Looks at a toy for several seconds', max_length=10, choices=YN_CHOICES, null=True)
    head = models.CharField('Holds head up when on tummy', max_length=10, choices=YN_CHOICES, null=True)
    move = models.CharField('Move both arms and both legs', max_length=10, choices=YN_CHOICES, null=True)
    hands = models.CharField('Opens hands briefly', max_length=10, choices=YN_CHOICES, null=True)


    def __str__(self):
       return str(self.user)
    

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

