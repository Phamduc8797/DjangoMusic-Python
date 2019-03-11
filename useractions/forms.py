from django import forms
from .models import Like, Comment, Contact, Lyric
from musics.models import Singer, Song

class ContactCreateForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'content',]

class UploadSongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['name', 'photo', 'urlsong', 'singer', 'category', 'description',]

class CreateLyricForm(forms.ModelForm):
    class Meta:
        model = Lyric
        fields = ['content',]

class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]

class CreateSingerForm(forms.ModelForm):
    class Meta:
        model = Singer
        fields = ['photo', 'name', 'description',]