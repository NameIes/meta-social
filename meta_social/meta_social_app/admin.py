'''
Admin module
'''

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *


class MusicAdmin(admin.ModelAdmin):
    list_display = ('user', 'artist', 'title', )


admin.site.register(Music, MusicAdmin)


class PostImagesInline(admin.TabularInline):
    min_num = 1
    max_num = 10
    model = PostImages


class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', )
    inlines = (PostImagesInline, )


admin.site.register(Post, PostAdmin)


class MessageInline(admin.StackedInline):
    model = Messages
    verbose_name_plural = 'Сообщения'
    fk_name = 'from_user'


class CommentInline(admin.StackedInline):
    model = Comment
    verbose_name_plural = 'Комментарии'


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Профиль'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, CommentInline, MessageInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
