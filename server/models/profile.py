from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from server.models.time_stamp_mixin import TimeStampMixin


class Profile(TimeStampMixin):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_server_key = models.BinaryField(max_length=50, blank=True)
    current_server_key_salt = models.BinaryField(max_length=50, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
