# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView
from .models import Comment, Contact, Like, Lyric
from musics.models import Singer, Category, Song
from .forms import ContactCreateForm, UploadSongForm, CreateLyricForm, CreateCommentForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from musics.views import DetailSongView

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
        print(Singer.objects.first())
        print(Category.objects.first())
        print(self.request.user)
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

class CreateCommentView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = '/login/'
    template_name = 'songs/song_detail.html'
    form_class = CreateCommentForm
    success_message = 'You have successfully commented.'

    def form_valid(self, form):
        get_song_id = Song.objects.get(pk=self.kwargs.get('pk'))
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.song = get_song_id
        return super(CreateCommentView, self).form_valid(form)

class DeleteLyricView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = '/login/'
    model = Lyric
    success_url = '/dashboard/list-lyrics/'
    success_message = 'Delete the lyric successfully.'

class DeleteSongView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = '/login/'
    model = Song
    success_url = '/list-songs'
    success_message = 'Delete the song successfully.'

class DeleteCommentView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = '/login/'
    model = Comment
    success_url = '/detail-song/1'
    success_message = 'Delete the comment successfully.'

class UpdateLyricView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = '/login/'
    model = Lyric
    template_name = 'admin/lyrics/edit_lyric.html'
    success_url = '/dashboard/list-lyrics/'
    success_message = 'Update the lyric successfully.'
    fields = ['content',]
