"""
Define and customise Forms
"""
from django.apps import AppConfig
from django import forms
from .models import Post, Category, Comment


choices = Category.objects.all().values_list('name', 'name')
choice_list = []

for item in choices:
    choice_list.append(item)


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
        fields = ('title', 'category', 'body', 'author',)

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "What's on your mind?"}),
            'category': forms.Select(choices=choice_list, attrs={
                'class': 'form-control'}),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Say something more..."}),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'value': '',
                'id': 'user_name',
                'type': 'hidden'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', 'name')
        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Type your comment here."}),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Type your comment here."})
        }