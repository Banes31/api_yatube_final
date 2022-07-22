from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import GenericViewSet

from posts.models import Group, Post

from .permissions import IsAuthoredOrReadOnly
from .serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer,
)


class CreateRetrieveViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet
):
    """Кастомный базовый класс вьюсета.
    Он будет создавать экземпляр объекта и получать экземпляр объекта.
    """
    pass


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для обработки GET запросов к эндпоинту groups/."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет для обработки CRUD запросов к эндпоинту posts/."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthoredOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('text', 'pub_date', 'author', 'group')
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет для обработки CRUD запросов к эндпоинту posts/.../comments/."""
    serializer_class = CommentSerializer
    permission_classes = (IsAuthoredOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('post', 'author')

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments


class FollowViewSet(CreateRetrieveViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__username', 'following__username')

    def get_queryset(self):
        return self.request.user.follower

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
