# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.db.models import F
from django.core.urlresolvers import reverse
from django.http import JsonResponse, HttpResponse

from django.core.mail import EmailMessage

from .models import Singer, Song, Category
from useractions.models import Lyric, Comment, Contact, Like
from django.contrib.auth.models import User

from django.template.loader import render_to_string

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

class DetailSongView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    model = Song
    template_name = 'songs/song_detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailSongView, self).get_context_data(**kwargs)
        # get_song_id = Song.objects.get(pk=self.kwargs.get('pk')).id
        get_song_id = self.kwargs.get('pk')
        user = self.request.user
        Song.objects.filter(id=get_song_id).update(listening=F('listening') + 1)
        # print(self.kwargs.get('pk'))
        # print(self.request.user)
        context['liked'] = Like.objects.filter(user=user,song=get_song_id)
        context['lyrics'] = Lyric.objects.filter(song=get_song_id, accept=True)[1:]
        context['lyricfirst'] = Lyric.objects.filter(song=get_song_id, accept=True).first()
        context['comments'] = Comment.objects.filter(song=get_song_id).order_by('-updated')
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
    lyr = Lyric.objects.get(id=pk)
    sog = lyr.song.name
    to_mail = lyr.user.email
    email = EmailMessage('[DjangoMusic] Accepted Lyric', 'Your '+sog+' lyrics has been approved.', to=[to_mail])
    email.send()
    return redirect('dashboards:list-lyrics')

def ignore_lyric(request, pk):
    Lyric.objects.filter(id=pk).update(accept=False)
    lyr = Lyric.objects.get(id=pk)
    sog = lyr.song.name
    to_mail = lyr.user.email
    email = EmailMessage('[DjangoMusic] Canceled Lyric', 'Your '+sog+' lyrics has been canceled.', to=[to_mail])
    email.send()
    return redirect('dashboards:list-lyrics')

def like_song(request, pk):
    user = request.user
    song = Song.objects.get(id=pk)
    like = Like(user=user, song=song)
    like.save()
    like_count = Like.objects.filter(song=song).count()
    return JsonResponse({'like_count': like_count})

def dislike_song(request, pk):
    user = request.user
    song = Song.objects.get(id=pk)
    like = Like.objects.filter(user=user, song=song)
    like.delete()
    like_count = Like.objects.filter(song=song).count()
    return JsonResponse({'like_count': like_count})

def delete_comment(request, pk, comment_id):
    user = request.user
    song = Song.objects.filter(id=pk)
    comment = Comment.objects.filter(id=comment_id, user=user)
    comment.delete()
    listcomments = Comment.objects.filter(song=song).order_by('-updated')
    html = render_to_string( 'songs/comments.html', { 'comments': listcomments, 'current_user': user, 'object': pk} )
    return HttpResponse( json.dumps(html), 'application/json' )
    