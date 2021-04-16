from django.db import models
from .posts import (Posts,
                    get_image_filename)


class Images(models.Model):
    post = models.ForeignKey(
        Posts,
        default=None,
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to=get_image_filename,
        verbose_name='Image'
    )

