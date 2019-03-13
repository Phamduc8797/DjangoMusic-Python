# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import CreateView
from .forms import RegisterForm

from django.contrib.messages.views import SuccessMessageMixin

from django.core.mail import EmailMessage

class RegisterView(SuccessMessageMixin, CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_message = 'You have sign up successfully. Lets Sign in.' 
    success_url = '/'