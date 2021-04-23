from rest_framework import serializers
from ..models import (
    Comments,
)


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comments
        fields = ['author', 'comment', 'added']
