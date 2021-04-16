from datetime import datetime
from django.db import models


class Comments(models.Model):
    author = models.CharField(
        max_length=25,
        default="Guest"
    )
    comment = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )
    added = models.DateField(default=datetime)

    def __str__(self):
        return self.comment
