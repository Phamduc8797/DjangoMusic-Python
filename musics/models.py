# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False)
    url = models.ImageField(upload_to='static/images/uploads')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(max_length=255, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Singer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.OneToOneField(Image)
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(max_length=255, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 

class Song(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.OneToOneField(Image)
    urlsong = models.FileField(upload_to='static/medias/uploads')
    name = models.CharField(max_length=255, null=False, blank=False)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(max_length=255, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 