from django.db import models
from django.db.models import base
from core import models as core_models
from users import models as user_models


class Post(core_models.TimeStampedModel):

    """Post Model Definition"""

    title = models.CharField(max_length=80, null=True, blank=True)
    writer = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True)
    body = models.TextField(null=True, blank=True)
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title[:30]
