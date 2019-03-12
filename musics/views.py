# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.db.models import F
from django.core.urlresolvers import reverse

from .models import Singer, Song, Category
from useractions.models import Lyric, Comment, Contact

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
        Song.objects.filter(id=get_song_id).update(listening=F('listening') + 1)
        # print(self.kwargs.get('pk'))
        # print(self.request.user)
        context['lyrics'] = Lyric.objects.filter(song=get_song_id, accept=True)[1:]
        context['lyricfirst'] = Lyric.objects.filter(song=get_song_id, accept=True).first()
        context['comments'] = Comment.objects.filter(song=get_song_id).order_by('-updated')[0:5] 
        context['lyrictotal'] = Lyric.objects.filter(song=get_song_id, accept=True)
        return context

class DashboardView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'admin/dashboards/dashboard.html'
        obj = {
            'songs': Song.objects.all(),
            'comments': Comment.objects.all(),
            'lyrics': Lyric.objects.all(),
            'singers': Singer.objects.all(),
            'categories': Category.objects.all(),
            'contacts': Contact.objects.all(),
        }
        return render(request, template_name, obj)

class DashboardSongView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'admin/songs/list-songs.html'
        obj = {
            'songs': Song.objects.all(),
        }
        return render(request, template_name, obj)

class DashboardCommentView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'admin/comments/list-comments.html'
        obj = {
            'comments': Comment.objects.all(),
        }
        return render(request, template_name, obj)

class DashboardLyricView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'admin/lyrics/list-lyrics.html'
        obj = {
            'lyrics': Lyric.objects.all(),
        }
        return render(request, template_name, obj)
        
class DashboardSingerView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'admin/singers/list-singers.html'
        obj = {
            'singers': Singer.objects.all().order_by('-updated'),
            'songs': Song.objects.all(),
        }
        return render(request, template_name, obj)

class DashboardCategoryView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'admin/categories/list-categories.html'
        obj = {
            'categories': Category.objects.all().order_by('-updated'),
            'songs': Song.objects.all(),
        }
        return render(request, template_name, obj)

class DashboardContactView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'admin/contacts/list-contacts.html'
        obj = {
            'contacts': Contact.objects.all(),
        }
        return render(request, template_name, obj)

def accept_lyric(request, pk):
    Lyric.objects.filter(id=pk).update(accept=True)
    return redirect('dashboards:list-lyrics')

def ignore_lyric(request, pk):
    Lyric.objects.filter(id=pk).update(accept=False)
    return redirect('dashboards:list-lyrics')