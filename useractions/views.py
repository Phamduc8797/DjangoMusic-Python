# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, DeleteView, UpdateView
from .models import Comment, Contact, Like, Lyric
from musics.models import Singer, Category, Song
from .forms import (
    ContactCreateForm, 
    UploadSongForm, 
    CreateLyricForm, 
    CreateCommentForm, 
    CreateSingerForm,
    AdminCreateCategoryForm,
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from musics.views import DetailSongView

from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse

from django.core.mail import EmailMessage

class ContactCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = '/login/'
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
            'listcontents': Contact.objects.all()[1:7],
            'firstcontact': Contact.objects.first()
        }
        return render(request, template_name, obj)

class UploadSongView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = '/login/'
    template_name = 'songs/upload-song.html'
    form_class = UploadSongForm
    success_message = 'Upload song successfully!'

    # def get_form_kwargs(self):
    #     kwargs = super(UploadSongView, self).get_form_kwargs()
    #     print(kwargs)
    #     return kwargs

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(UploadSongView, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        template_name = 'songs/upload-song.html'
        obj = {
            'singers': Singer.objects.all(),
            'categories': Category.objects.all()
        }        
        return render(request, template_name, obj)

class CreateLyricView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = '/login/'
    template_name = 'songs/song_detail.html'
    form_class = CreateLyricForm
    success_message = 'Contribute lyric successfully!. Pls waiting admin approved.'

    def form_valid(self, form):
        get_song_id = Song.objects.get(pk=self.kwargs.get('pk'))
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.song = get_song_id
        return super(CreateLyricView, self).form_valid(form)
    
    def get_success_url(self): 
        return reverse('detail-song', kwargs={'pk': self.kwargs.get('pk')})

class CreateCommentView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = '/login/'
    template_name = 'songs/song_detail.html'
    form_class = CreateCommentForm
    success_message = 'You have successfully commented.'

    def form_valid(self, form):
        get_song_id = self.kwargs.get('pk')
        get_song = Song.objects.get(pk=get_song_id)
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.song = get_song
        if form.is_valid():
            if self.request.is_ajax():
                form.save()
                user = self.request.user
                listcomments = Comment.objects.filter(song=get_song).order_by('-updated')
                html = render_to_string( 'songs/comments.html', { 'comments': listcomments, 'current_user': user, 'object': get_song_id} )
                return HttpResponse( json.dumps(html), 'application/json' )
        else:
            return super(CreateCommentView, self).form_valid(form)        
    


class CreateSingerView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = '/login/'
    template_name = 'admin/singers/create_singer.html'
    form_class = CreateSingerForm
    success_message = 'Singer has been created.'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(CreateSingerView, self).form_valid(form)
    
    def get_success_url(self): 
        return reverse('dashboards:list-singers', kwargs={})

class AdminCreateCategoryView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = '/login/'
    template_name = 'admin/categories/create_category.html'
    form_class = AdminCreateCategoryForm
    success_message = 'Category has been created.'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(AdminCreateCategoryView, self).form_valid(form)
    
    def get_success_url(self): 
        return reverse('dashboards:list-categories', kwargs={})

class DeleteLyricView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = '/login/'
    model = Lyric
    success_message = 'Delete the lyric successfully.'
    template_name = 'admin/confirms/confirm_delete.html'

    def get_success_url(self): 
        return reverse('dashboards:list-lyrics', kwargs={})

class AdminDeleteSingerView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = '/login/'
    model = Singer
    success_message = 'Delete the singer successfully.'
    template_name = 'admin/confirms/confirm_delete.html'

    def get_success_url(self): 
        return reverse('dashboards:list-singers', kwargs={})

class AdminDeleteCategoryView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = '/login/'
    model = Category
    success_message = 'Delete the category successfully.'
    template_name = 'admin/confirms/confirm_delete.html'

    def get_success_url(self): 
        return reverse('dashboards:list-categories', kwargs={})

class AdminDeleteContactView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = '/login/'
    model = Contact
    success_message = 'Delete the contact successfully.'
    template_name = 'admin/confirms/confirm_delete.html'

    def get_success_url(self): 
        return reverse('dashboards:list-contacts', kwargs={})

class AdminDeleteCommentView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = '/login/'
    model = Comment
    success_message = 'Delete the comment successfully.'
    template_name = 'admin/confirms/confirm_delete.html'

    def get_success_url(self): 
        return reverse('dashboards:list-comments', kwargs={})

class AdminDeleteSongView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = '/login/'
    model = Song
    success_message = 'Delete the song successfully.'
    template_name = 'admin/confirms/confirm_delete.html'

    def get_success_url(self): 
        return reverse('dashboards:list-song', kwargs={})

class UpdateLyricView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = '/login/'
    model = Lyric
    template_name = 'admin/lyrics/edit_lyric.html'
    success_message = 'Update the lyric successfully.'
    fields = ['content',]

    def get_success_url(self): 
        return reverse('dashboards:list-lyrics', kwargs={})

class AdminUpdateSingerView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = '/login/'
    model = Singer
    template_name = 'admin/singers/edit_singer.html'
    success_message = 'Update the singer successfully.'
    fields = ['photo', 'name', 'description',]

    def get_success_url(self): 
        return reverse('dashboards:list-singers', kwargs={})

class AdminUpdateCategoryView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = '/login/'
    model = Category
    template_name = 'admin/categories/edit_category.html'
    success_message = 'Update the category successfully.'
    fields = ['photo', 'name', 'description',]

    def get_success_url(self): 
        return reverse('dashboards:list-categories', kwargs={})

class AdminUpdateSongView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = '/login/'
    model = Song
    template_name = 'admin/songs/edit_song.html'
    success_message = 'Update the song successfully.'
    fields = ['photo', 'name', 'description', 'urlsong', 'singer', 'category']

    def get_success_url(self): 
        return reverse('dashboards:list-song', kwargs={})

    def get_context_data(self, **kwargs):
        context = super(AdminUpdateSongView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['singers'] = Singer.objects.all()
        return context
