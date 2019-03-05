# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from musics.models import Song
from django.core.urlresolvers import reverse

User = settings.AUTH_USER_MODEL

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.TextField(max_length=250, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
    def get_absolute_url(self):
        return reverse('detail-song', kwargs={'pk': 1})
        
class Contact(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    content = models.TextField(max_length=254, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
    
    def get_absolute_url(self):
        return reverse('contactview', kwargs={})

class Lyric(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.TextField(null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('detail-song', kwargs={'pk': 1})
