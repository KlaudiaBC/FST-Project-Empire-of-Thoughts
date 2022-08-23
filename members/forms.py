"""
Define and customise Forms
"""
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    """
    Add customised input field for an email
    to the default django registration form
    """
    email = forms.EmailField(required=True)
    agree = forms.BooleanField(label="Agreement required:")

    class Meta:
        """
        Specify the input fields for registration form
        """
        model = User
        fields = ('username', 'email', 'password1', 'password2', "agree")

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
