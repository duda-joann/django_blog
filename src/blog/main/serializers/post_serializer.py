from rest_framework import serializers
from .notes_serializer import NoteSerializer
from ..models import Post


class PostSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name = 'detail',
        lookup_field = 'slug',
    )

    class Meta:
        model = Post
        fields = ['id',
                  'title',
                  'thumbnail',
                  'url', ]


class PostDetailSerializer(serializers.ModelSerializer):
    notes = NoteSerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'


class PostCreateUpdateSerializer(serializers.ModelSerializer):
    notes = NoteSerializer(many=True)

    class Meta:
        model = Post
        fields = [
                    'title',
                    'thumbnail',
                    'categories',
                    'published',
                    'notes',
                ]
