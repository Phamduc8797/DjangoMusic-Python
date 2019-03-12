# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from musics.models import Song
from django.core.urlresolvers import reverse

User = settings.AUTH_USER_MODEL

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_likes')
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='song_likes')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.user

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='song_comments')
    content = models.TextField(max_length=250, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.content

    def truncatecontent(self):
        trunc = self.content
        if len(trunc)>40:
            lyr = trunc[0:40] + "..."
        else:
            lyr = trunc[0:40]
        return lyr
        
class Contact(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    content = models.TextField(max_length=254, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.content
    
    def get_absolute_url(self):
        return reverse('contactview', kwargs={})

    def get_content(self):
        trunc = self.content
        if len(trunc)>40:
            cont = trunc[0:40] + "..."
        else:
            cont = trunc[0:40]
        return cont

class Lyric(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_lyrics')
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='song_lyrics')
    content = models.TextField(null=False, blank=False)
    accept = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.content

    def truncatecontent(self):
        trunc = self.content
        if len(trunc)>40:
            lyr = trunc[0:40] + "..."
        else:
            lyr = trunc[0:40]
        return lyr

    def abc(self):
        print(self.user.username)
