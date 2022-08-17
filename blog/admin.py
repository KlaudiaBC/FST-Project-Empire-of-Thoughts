"""
Create permissions and setting for the Admin Panel
"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Customise the Add Post form in the Admin Panel.
    Args: SummernoteModelAdmin (body): Add tools for
    editing a text in the test field
    """
    list_display = ('title', 'author')
    search_fields = ['title', 'content']
    summernote_fields = ('body',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Give Admin a permission to aprove
    the comment or delete it.
    """
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
