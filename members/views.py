"""
Define and customise Views
"""
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView
from .forms import SignUpForm


class UserRegisterView(CreateView):
    """
    Define attributes for the registration form,
    which will render in specyfied html file.
    """
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    # this method enable message to display after form was submitted
    def form_valid(self, form):
        messages.success(self.request, 'Account created successfully!')
        return super().form_valid(form)


def terms_view(request):
    """
    Returns the Terms and Conditions page
    """
    return render(request, 'registration/terms.html')
