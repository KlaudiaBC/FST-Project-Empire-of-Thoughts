"""
Create permissions and setting for the Admin Panel
"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Customise the Add Post form.
    Args: SummernoteModelAdmin (body): Add tools for
    editing a text in the test field
    """
    list_display = ('title', 'author')
    search_fields = ['title', 'content']
    summernote_fields = ('body')
