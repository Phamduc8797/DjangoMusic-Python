# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Like, Comment, Contact, Lyric

# admin.site.register(Like)
# admin.site.register(Comment)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'song', 'timestamp', 'updated')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'user', 'song', 'timestamp', 'updated')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'name', 'email', 'timestamp', 'updated')

@admin.register(Lyric)
class LyricAdmin(admin.ModelAdmin):
    list_display = ('content', 'song', 'user', 'accept', 'timestamp', 'updated')
