from rest_framework import serializers
from ..models import (
    Notes,
)


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notes
        fields = ['header', 'image', 'text', 'created_date']
