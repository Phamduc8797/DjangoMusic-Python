# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings

from .models import Singer, Song
from useractions.models import Lyric, Comment

after_logout = settings.LOGOUT_REDIRECT_URL

class HomeView(ListView):
    login_url = '/login/'
    def get(self, request, *args, **kwargs):
        return render(request, "homes/home.html", {})

class LogoutView(LoginRequiredMixin, LogoutView):
    login_url = '/login/'
    next_page = after_logout

class ListSingerView(ListView):
    model = Singer       
    def get(self, request, *args, **kwargs):
        template_name = 'singers/list-singer.html'
        obj = {
            'listcontents': Singer.objects.all()
        }
        return render(request, template_name, obj)

class ListSongView(ListView):
    model = Song
    def get(self, request, *args, **kwargs):
        template_name = 'songs/list-songs.html'
        obj = {
            'songs': Song.objects.all()
        }
        return render(request, template_name, obj)

class DetailSongView(DetailView):
    model = Song
    template_name = 'songs/song_detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailSongView, self).get_context_data(**kwargs)
        # get_song_id = Song.objects.get(pk=self.kwargs.get('pk')).id
        get_song_id = self.kwargs.get('pk')
        # print(self.kwargs.get('pk'))
        # print(self.request.user)
        context['lyrics'] = Lyric.objects.filter(song=get_song_id)[1:]
        context['lyricfirst'] = Lyric.objects.filter(song=get_song_id).first()
        context['comments'] = Comment.objects.filter(song=get_song_id)        
        return context
