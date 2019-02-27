# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import CreateView
from .models import Comment, Contact, Like
from .forms import ContactCreateForm

class ContactCreateView(CreateView):
    template_name = 'contacts/contact.html'
    form_class = ContactCreateForm

    def get_form_kwargs(self):
        kwargs = super(ContactCreateView, self).get_form_kwargs()
        # kwargs['user'] = self.request.user
        # kwargs['instance'] = Item.objects.filter(user=self.request.user).first()
        return kwargs

    def get_queryset(self):
        return Contact.objects.all()

    def form_valid(self, form):
        obj = form.save(commit=False)
        # obj.user = self.request.user
        return super(ContactCreateView, self).form_valid(form)

    def get_context_data(self,*args, **kwargs):
        context = super(ContactCreateView, self).get_context_data(*args, **kwargs)
        # context['title'] = 'Create Contact'
        return context

    def get(self, request, *args, **kwargs):
        template_name = 'contacts/contact.html'
        obj = {
            'listcontents': Contact.objects.all()
        }
        return render(request, template_name, obj)