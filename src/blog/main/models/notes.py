from django.db import models
from .post import (Post,
                   get_image_filename)


class Notes(models.Model):
    header = models.CharField(
        max_length=50,
        blank=True, null=True
    )
    post = models.ForeignKey(
        Post,
        related_name= 'notes',
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to=get_image_filename,
        verbose_name='Image'
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

    class Meta:
        db_table = 'notes'

    def __str__(self):
        return f'{self.post}, {self.header},' \
               f' {self.image}, {self.text},' \
               f' {self.created_date}, {self.last_modified}'