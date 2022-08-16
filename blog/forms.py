"""
Define and customise Forms
"""
from django.apps import AppConfig
from django import forms
from .models import Post


class BlogConfig(AppConfig):
    """
    Automatic configuration
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'


class PostForm(forms.ModelForm):
    """
    Settings for the Post form
    """
    class Meta:
        """
        Add the bootstrap "form-control" class for styling
        """
        model = Post
        fields = ('title', 'body', 'author')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "What's on your mind?"}),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Say something more..."}),
        }
