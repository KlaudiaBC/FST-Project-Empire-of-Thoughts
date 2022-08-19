"""
Create permissions and setting for the Admin Panel
"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Category


@admin.register(Post)
@admin.register(Category)


class PostAdmin(SummernoteModelAdmin):
    """
    Customise the Add Post form in the Admin Panel.
    Args: SummernoteModelAdmin (body): Add tools for
    editing a text in the test field
    """
    search_fields = ['title', 'content']
    summernote_fields = ('body',)
