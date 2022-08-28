"""
Define and customise Views
"""
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib import messages
from .forms import SignUpForm, UserCreationForm


# class UserRegisterView(generic.CreateView):
#     """
#     Define attributes for the registration form,
#     which will render in specyfied html file.
#     """
#     form_class = SignUpForm
#     template_name = 'registration/register.html'
#     success_url = reverse_lazy('login')

#     # this method enable message to display after form was submitted
#     def form_valid(self, form):
#         messages.success(self.request, 'Account created successfully!')
#         return super().form_valid(form)


def signup(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        messages.success(request, 'Account created successfully!')
        return super().form_valid(form)
    else:
        form = SignUpForm()
        
    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context)


def terms_view(request):
    """
    Returns the Terms and Conditions page
    """
    return render(request, 'registration/terms.html')
