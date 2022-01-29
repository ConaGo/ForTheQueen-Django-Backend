from base64 import b64decode
from base64 import b64encode
import hashlib
import os

from django.contrib.sessions.models import Session
from django.core.exceptions import PermissionDenied
from django.db import transaction
from django.http import HttpRequest
from django.http import HttpResponse

from server.models.profile import Profile
from server.models.user_session import UserSession


class ServerAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):

        if "/api" in request.path:
            try:
                username = request.headers["FTQ-Username"]
                server_key = request.headers["Server-Key"]

                profile = Profile.objects.get(user__username=username)  # type: Profile
                check_key = hashlib.pbkdf2_hmac(
                    "sha256",
                    b64decode(server_key.encode("utf-8")),
                    profile.current_server_key_salt,
                    100_000,
                )
                if not bytes(profile.current_server_key) == check_key:
                    raise PermissionDenied
            except:
                raise PermissionDenied

        response = self.get_response(request)  # type: HttpResponse

        if "/login" in request.path and request.user.is_authenticated:
            # Log out user from all other sessions
            with transaction.atomic():
                session = Session.objects.get(session_key=request.session.session_key)
                user_sessions = UserSession.objects.filter(user=request.user).exclude(
                    session=session
                )
                for user_session in user_sessions:
                    user_session.session.delete()
                UserSession.objects.get_or_create(
                    user=request.user, session_id=request.session.session_key
                )

                # Set new server-key
                profile = Profile.objects.get(user=request.user)
                server_key = os.urandom(32)
                salt = os.urandom(32)
                encrypted_key = hashlib.pbkdf2_hmac("sha256", server_key, salt, 100_000)
                profile.current_server_key = encrypted_key
                profile.current_server_key_salt = salt
                profile.save()
                print(b64encode(server_key).decode("utf-8"))
            response.headers["Set-Server-Key"] = b64encode(server_key).decode("utf-8")

        return response
