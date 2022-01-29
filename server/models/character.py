from django.db import models

from server.models.time_stamp_mixin import TimeStampMixin


class Character(TimeStampMixin):
    hp_max = models.PositiveIntegerField()
    hp_current = models.PositiveIntegerField()

    class ClassType(models.TextChoices):
        DEFAULT = "DEFAULT"
        WARRIOR = "WARRIOR"
        RANGER = "RANGER"
        WIZARD = "WIZARD"

    class_type = models.CharField(
        max_length=20, choices=ClassType.choices, default=ClassType.DEFAULT
    )
