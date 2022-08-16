"""
Define and customise Views
"""
from django.views import generic
from django.urls import reverse_lazy
from .forms import SignUpForm


class UserRegisterView(generic.CreateView):
    """
    Define attributes for the registration form,
    which will render in specyfied html file.
    """
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
