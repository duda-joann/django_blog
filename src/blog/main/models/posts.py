from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from .categories import Categories


class Posts(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=50, blank=False, null = False,
        default="Title Of Your Post"
    )
    text = models.TextField(
        blank=False, null=False,
        default="Put your text here"
    )
    published = models.BooleanField(default=False)
    categories = models.CharField(
        max_length=50,
        choices=Categories.choices,
        default=Categories.LIFESTYLE
    )


def get_image_filename(instance, filename):
    title = instance.post.title
    slug = slugify(title)
    return f'post_images/%s-%s' % (slug, filename)

