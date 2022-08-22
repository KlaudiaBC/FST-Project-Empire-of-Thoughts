"""
Define the URLs for the 'blog' application
"""
from django.urls import path, include
from .views import UserRegisterView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('members/', include('django.contrib.auth.urls')),
    path('terms/', include('termsandconditions.urls')),
]
