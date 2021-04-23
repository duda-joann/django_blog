from datetime import datetime
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class CommentManager(models.Manager):
    def all(self):
        qs = super(CommentManager, self).filter(parent=None)
        return qs

    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model()
        obj_id = instance.id
        qs = super(CommentManager, self) \
            .filter(content_type=content_type, object_id=obj_id) \
            .filter(parent=None)
        return qs


class Comments(models.Model):
    content_type = models.ForeignKey(
        ContentType,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(
        'content_type',
        'object_id'
    )
    parent = models.ForeignKey('self',null=True, blank=True, on_delete=models.CASCADE)
    author = models.CharField(
        max_length=25,
        default="Guest"
    )
    comment = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    added = models.DateField(
        default=datetime
    )
    objects = CommentManager()

    class Meta:
        db_table = 'comments'
        ordering = ['-added']

    def __str__(self):
        return f' {self.comment}, {self.object_id}, {self.added}, {self.author}'
