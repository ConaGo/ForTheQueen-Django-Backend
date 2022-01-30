from django.db import models

from server.models.savestate import Savestate
from server.models.time_stamp_mixin import TimeStampMixin


class Character(TimeStampMixin):
    hp_max = models.PositiveIntegerField()
    hp_current = models.PositiveIntegerField()
    savestate = models.ForeignKey(Savestate, on_delete=models.CASCADE, related_name="characters")
    level = models.PositiveIntegerField(default=1)

    class ClassType(models.TextChoices):
        DEFAULT = "DEFAULT"
        WARRIOR = "WARRIOR"
        RANGER = "RANGER"
        WIZARD = "WIZARD"

    class_type = models.CharField(
        max_length=20, choices=ClassType.choices, default=ClassType.DEFAULT
    )

    def __str__(self):
        return f"{self.class_type} level: {self.level} - HP: {self.hp_current}/{self.hp_max}"
