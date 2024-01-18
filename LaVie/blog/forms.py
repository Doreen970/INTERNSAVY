# a form used to create articles

from django import forms
from .models import Article
from ckeditor.widgets import CKEditorWidget

class BlogForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'image']
        widgets = {
            'content': CKEditorWidget(),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'image']
        widgets = {
            'content': CKEditorWidget(),
        }