from django.contrib.auth import user_logged_in
from django.contrib.auth import user_logged_out
from django.dispatch import receiver
from django.http import HttpRequest

from server.models import Profile


@receiver(user_logged_out)
def logout_hook(sender, request: HttpRequest, user, **kwargs):
    profile = Profile.objects.get(user=user)  # type: Profile
    profile.current_server_key = b""
    profile.current_server_key_salt = b""
    profile.save()
