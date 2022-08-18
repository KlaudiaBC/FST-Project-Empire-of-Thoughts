"""
Define the URLs for the project empire-blog
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('', include('blog.urls'), name="blog_urls"),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls'), name="members_urls"),
]
