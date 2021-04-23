from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from .categories import Categories
from .comments import Comments


class Post(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=50, blank=False, null = False,
        default="Title Of Your Post"
    )
    thumbnail = models.ImageField(upload_to='post_images/%Y/%m/%d/')
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    categories = models.CharField(
        max_length=50,
        choices=Categories.choices,
        default=Categories.LIFESTYLE)
    comments = GenericRelation(Comments, related_query_name='post')

    class Meta:
        db_table = 'post'
        ordering = ['created']

    @property
    def get_comments(self):
        instance = self
        qs = Comments.objects.filter_by_instance(instance)
        return qs

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type

    def __str__(self):
        return f'{self.id}, {self.title}, {self.categories}, {self.slug}, {self.created}, {self.published}'


def get_image_filename(instance, filename):
    title = instance.post.title
    slug = slugify(title)
    return f'post_images/%s-%s' % (slug, filename)

