"""djangoMusic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from users.views import RegisterView
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from musics.views import HomeView, LogoutView, ListSingerView, ListSongView, DetailSongView, DashboardLyricView
from useractions.views import (
    ContactCreateView, 
    UploadSongView, 
    CreateLyricView, 
    CreateCommentView, 
    DeleteLyricView,
)
from useractions.models import Lyric
from musics import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),

    url(r'^list-singer/$', ListSingerView.as_view(), name='list-singer'),
    url(r'^list-songs/$', ListSongView.as_view(), name='list-songs'),
    
    url(r'^upload-song/$', UploadSongView.as_view(), name='upload-song'),

    url(r'^contact/$', ContactCreateView.as_view(), name='contactview'),

    url(r'^detail-song/(?P<pk>[-\w]+)$', DetailSongView.as_view(), name='detail-song'),

    url(r'^create-lyric/(?P<pk>[-\w]+)$', CreateLyricView.as_view(), name='create-lyric'),
    url(r'^create-comment/(?P<pk>[-\w]+)$', CreateCommentView.as_view(), name='create-comment'),

    url(r'^detail-song/(?P<pk>[-\w]+)/delete-comment/(?P<comment_id>[-\w]+)$', views.delete_comment, name='delete-comment'),
    
    url(r'^like-song/(?P<pk>[-\w]+)$', views.like_song, name='like-song'),
    url(r'^dislike-song/(?P<pk>[-\w]+)$', views.dislike_song, name='dislike-song'),

    url(r'^dashboard/', include('useractions.urls', namespace='dashboards')),
]
