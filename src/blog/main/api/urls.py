from django.conf.urls import url
from .views import (
    PostListApiView,
    PostDetailApiView,
    PostDeleteApiView,
    PostCreateApiView,
    PostUpdateApiView)

urlpatterns = [
    url(r'^$', PostListApiView.as_view(), name='post-list'),
    url(r'^(?P<slug>[\w-]+)/$', PostDetailApiView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/new', PostCreateApiView.as_view(), name='new'),
    url(r'^(?P<slug>[\w-]+)/edit', PostUpdateApiView.as_view(), name='edit'),
    url(r'^(?P<slug>[\w-]+)/delete', PostDeleteApiView.as_view(), name='delete')
]