from django.db import models
from .posts import Posts


class Notes(models.Model):
    header = models.CharField(
        max_length=50,
        blank=True, null=True
    )
    post = models.ForeignKey(
        Posts, default=None,
        on_delete=models.CASCADE
    )
    text = models.TextField(
        null=True,
        blank=True
    )
    created_date = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )
