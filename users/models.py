# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class CustomUser(models.Model):
    user = models.OneToOneField(User)
    photo = models.ImageField(upload_to='static/images/uploads/users', null=True, blank=True)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email