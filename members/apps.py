"""
Define installed apps
"""
from django.apps import AppConfig


class MembersConfig(AppConfig):
    """
    App configuration
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'members'
