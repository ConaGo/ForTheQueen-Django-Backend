from django.db import models

from server.models.profile import Profile


class Savestate(models.Model):

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Level(models.TextChoices):
        DEFAULT = "DE"
        DUNGEON_1 = "D1"

    current_level = models.CharField(max_length=2, choices=Level.choices, default=Level.DEFAULT)
