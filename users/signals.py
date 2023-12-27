from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from.models import Profile
# when a user is saved, it sends a signal and this reciever will recieves it.
@receiver (post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created: #if the user was created it will also create the profile for the particuar user.
        Profile.objects.create(user=instance)
        
@receiver (post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()
   