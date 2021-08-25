from django.contrib import admin
from . import models


@admin.register(models.Post)
class PostModelAdmin(admin.ModelAdmin):

    """Post Model Admin Definition"""

    list_display = (
        "title",
        "writer",
    )
