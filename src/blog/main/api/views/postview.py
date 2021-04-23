from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView,
                                     CreateAPIView,
                                     UpdateAPIView,
                                     DestroyAPIView, )
from ...models import Post
from ... import serializers


class PostListApiView(ListAPIView):
    serializer_class = serializers.PostSerializer

    def get_queryset(self):
        qs = Post.objects.all()
        return qs


class PostDetailApiView(RetrieveAPIView):
    serializer_class = serializers.PostDetailSerializer
    queryset = Post.objects.all()
    lookup_field = 'slug'


class PostCreateApiView(CreateAPIView):
    serializer_class = serializers.PostCreateUpdateSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostUpdateApiView(UpdateAPIView):
    serializer_class = serializers.PostCreateUpdateSerializer
    queryset = Post.objects.all()
    lookup_field = 'slug'

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class PostDeleteApiView(DestroyAPIView):
    serializer_class = serializers.PostDetailSerializer
    queryset = Post.objects.all()
    lookup_field = 'slug'

