from django.db import models


class TimeStampedModel(models.Model):

    """Time Stamed Model Definition"""

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        abstract = True
