"""
Define the URLs for the project empire-blog
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('blog.urls'), name="blog_urls"),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls'), name="members_urls"),
    path(r'^media/(?P<path>.*)$', serve,
         {'document_root': settings.MEDIA_ROOT}),
    path(r'^static/(?P<path>.*)$', serve,
         {'document_root': settings.STATIC_ROOT}),
]

handler404 = "blog.views.handler404"
handler500 = "blog.views.handler500"
