# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

User = settings.AUTH_USER_MODEL

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False)
    photo = models.ImageField(upload_to='static/images/uploads', blank=True, default="static/images/default.png")
    description = models.TextField(max_length=255, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_description(self):
        trunc = self.description
        if trunc:
            if len(trunc)>40:
                descp = trunc[0:40] + "..."
            else:
                descp = trunc[0:40]
            return descp
        else:
            return "N/A"

class Singer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='static/images/uploads', blank=True, default="static/images/default.png")
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(max_length=255, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_description(self):
        trunc = self.description
        if trunc:
            if len(trunc)>40:
                descp = trunc[0:40] + "..."
            else:
                descp = trunc[0:40]
            return descp
        else:
            return "N/A"

class Song(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='static/images/uploads', blank=True, default="static/images/default.png")
    urlsong = models.FileField(upload_to='static/medias/uploads')
    listening = models.IntegerField(default=0)
    name = models.CharField(max_length=255, null=False, blank=False)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(max_length=255, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse('detail-song', kwargs={'pk': self.id})