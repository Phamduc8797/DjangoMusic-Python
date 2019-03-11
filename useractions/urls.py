from django.conf.urls import url
from django.contrib import admin
from users.views import RegisterView
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from musics.views import (
    DashboardView, 
    DashboardSongView, 
    DashboardCommentView, 
    DashboardLyricView,
    DashboardSingerView,
    DashboardCategoryView,
    DashboardContactView,
)
from .views import (
    CreateSingerView,
    AdminCreateCategoryView,

    UpdateLyricView,
    AdminUpdateSingerView,    
    AdminUpdateCategoryView,
    AdminUpdateSongView,

    DeleteLyricView,
    AdminDeleteContactView,
    AdminDeleteSingerView,
    AdminDeleteCategoryView,
    AdminDeleteCommentView,
    AdminDeleteSongView,
)
from musics import views

urlpatterns = [
    url(r'^$', DashboardView.as_view(), name='dashboard'),
    url(r'^list-songs/$', DashboardSongView.as_view(), name='list-song'),
    url(r'^list-comments/$', DashboardCommentView.as_view(), name='list-comments'),
    url(r'^list-lyrics/$', DashboardLyricView.as_view(), name='list-lyrics'),
    url(r'^list-singers/$', DashboardSingerView.as_view(), name='list-singers'),
    url(r'^list-categories/$', DashboardCategoryView.as_view(), name='list-categories'),
    url(r'^list-contacts/$', DashboardContactView.as_view(), name='list-contacts'),

    url(r'^accept-lyric/(?P<pk>[-\w]+)$', views.accept_lyric, name='accept-lyric'),
    url(r'^ignore-lyric/(?P<pk>[-\w]+)$', views.ignore_lyric, name='ignore-lyric'),

    url(r'^create-singer/$', CreateSingerView.as_view(), name='create-singer'),
    url(r'^create-category/$', AdminCreateCategoryView.as_view(), name='create-category'),

    url(r'^edit-lyric/(?P<pk>[-\w]+)$', UpdateLyricView.as_view(), name='edit-lyric'),
    url(r'^edit-singer/(?P<pk>[-\w]+)$', AdminUpdateSingerView.as_view(), name='edit-singer'),
    url(r'^edit-category/(?P<pk>[-\w]+)$', AdminUpdateCategoryView.as_view(), name='edit-category'),
    url(r'^edit-song/(?P<pk>[-\w]+)$', AdminUpdateSongView.as_view(), name='edit-song'),

    url(r'^delete-lyric/(?P<pk>[-\w]+)$', DeleteLyricView.as_view(), name='delete-lyric'),
    url(r'^delete-singer/(?P<pk>[-\w]+)$', AdminDeleteSingerView.as_view(), name='delete-singer'),
    url(r'^delete-contact/(?P<pk>[-\w]+)$', AdminDeleteContactView.as_view(), name='delete-contact'),
    url(r'^delete-category/(?P<pk>[-\w]+)$', AdminDeleteCategoryView.as_view(), name='delete-category'),
    url(r'^delete-comment/(?P<pk>[-\w]+)$', AdminDeleteCommentView.as_view(), name='delete-comment'),
    url(r'^delete-song/(?P<pk>[-\w]+)$', AdminDeleteSongView.as_view(), name='delete-song'),
]

