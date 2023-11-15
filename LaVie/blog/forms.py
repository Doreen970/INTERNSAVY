# a form used to create articles

from django import forms
from .models import Article

class BlogForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
