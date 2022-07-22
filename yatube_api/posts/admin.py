from django.contrib import admin

from .models import Comment, Follow, Group, Post
from yatube_api.settings import EMPTY_VALUE_DISPLAY


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Администрирование постов в панели администратора."""
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
        'image'
    )
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = EMPTY_VALUE_DISPLAY


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    """Администрирование групп в панели администратора."""
    list_display = ('title',)
    empty_value_display = EMPTY_VALUE_DISPLAY


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Администрирование комментариев в панели администратора."""
    list_display = (
        'post',
        'text',
        'author',
        'created'
    )
    search_fields = ('text',)
    list_filter = ('created',)
    empty_value_display = EMPTY_VALUE_DISPLAY


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    """Администрирование подписок в панели администратора."""
    list_display = (
        'user',
        'following'
    )
    search_fields = ('user',)
    list_filter = ('following',)
    empty_value_display = EMPTY_VALUE_DISPLAY
