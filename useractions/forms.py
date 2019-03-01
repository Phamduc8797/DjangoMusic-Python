from django import forms
from .models import Like, Comment, Contact, Song

class ContactCreateForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'content',]

class UploadSongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['name', 'photo', 'urlsong', 'singer', 'category', 'description',]