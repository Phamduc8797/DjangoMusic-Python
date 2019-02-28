from django.forms import ModelForm
from .models import Like, Comment, Contact

class ContactCreateForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'content',]
