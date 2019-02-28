# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import CreateView
from .models import Comment, Contact, Like
from .forms import ContactCreateForm
from django.contrib.messages.views import SuccessMessageMixin

class ContactCreateView(SuccessMessageMixin, CreateView):
    template_name = 'contacts/contact.html'
    form_class = ContactCreateForm
    success_message = 'Send contact successfully!'

    # def get_success_message(self, cleaned_data):
    #     return self.success_message % dict(
    #         cleaned_data,
    #     )
    
    # def get_form_kwargs(self):
    #     kwargs = super(ContactCreateView, self).get_form_kwargs()
    #     # kwargs['user'] = self.request.user
    #     # kwargs['instance'] = Item.objects.filter(user=self.request.user).first()
    #     print(kwargs)
    #     return kwargs

    # def get_queryset(self):
    #     return Contact.objects.all()

    # def form_valid(self, form):
    #     obj = form.save(commit=False)
    #     # obj.user = self.request.user
    #     return super(ContactCreateView, self).form_valid(form)

    # def get_context_data(self,*args, **kwargs):
    #     context = super(ContactCreateView, self).get_context_data(*args, **kwargs)
    #     context['mess'] = 'Create Contact'
    #     print(context)
    #     return context

    def get(self, request, *args, **kwargs):
        template_name = 'contacts/contact.html'
        obj = {
            'listcontents': Contact.objects.all()[:7]
        }
        return render(request, template_name, obj)