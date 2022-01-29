from django.db import models


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField("date_created", auto_now_add=True)
    updated_at = models.DateTimeField("last_modified", auto_now=True)

    class Meta:
        abstract = True
