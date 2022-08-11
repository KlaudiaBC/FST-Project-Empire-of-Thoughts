from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'author')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "What's on your mind?"}),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Say something more..."}),
            'author': forms.Select(attrs={'class': 'form-control'}),
        }
