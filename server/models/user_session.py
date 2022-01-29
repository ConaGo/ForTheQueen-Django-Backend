from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.db import models


class UserSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
