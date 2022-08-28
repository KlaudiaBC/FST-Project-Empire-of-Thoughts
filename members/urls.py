"""
Define the URLs for the 'blog' application
"""
from django.urls import path, include
from .views import signup, terms_view

urlpatterns = [
    path('register/', signup, name='register'),
    path('members/', include('django.contrib.auth.urls')),
    path('terms/', terms_view, name='terms')
]
