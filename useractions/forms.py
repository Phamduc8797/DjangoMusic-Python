from django import forms
from .models import Like, Comment, Contact, Song, Lyric

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