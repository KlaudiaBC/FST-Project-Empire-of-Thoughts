"""
Create permissions and setting for the Admin Panel
"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Category, Comment


@admin.register(Category)

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Customise the Add Post form in the Admin Panel.
    Args: SummernoteModelAdmin (body): Add tools for
    editing a text in the test field
    """
    search_fields = ['title', 'body']
    summernote_fields = ('body',)
    search_fields = ['title', 'category']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, queryset):
        queryset.update(approved=True)
        