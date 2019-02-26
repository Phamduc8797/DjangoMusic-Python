# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings

after_logout = settings.LOGOUT_REDIRECT_URL

class HomeView(ListView):
    login_url = '/login/'
    def get(self, request, *args, **kwargs):
        return render(request, "homes/home.html", {})

class LogoutView(LoginRequiredMixin, LogoutView):
    next_page = after_logout