# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Category, Singer, Song

# admin.site.register(Image)
# admin.site.register(Category)
# admin.site.register(Singer)
# admin.site.register(Song)

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'photo', 'singer', 'urlsong', 'listening', 'category', 'description', 'timestamp', 'updated')

@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'photo', 'description', 'timestamp', 'updated')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'photo', 'description', 'timestamp', 'updated')