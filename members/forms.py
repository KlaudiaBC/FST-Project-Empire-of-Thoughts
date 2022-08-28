"""
Define and customise Forms
"""
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    """
    Add customised input field for an email
    to the default django registration form
    """
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs('class', 'form-control')
        self.fields['email'].widget.attrs('class', 'form-control')
        self.fields['password1'].widget.attrs('class', 'form-control')
        self.fields['password2'].widget.attrs('class', 'form-control')

    class Meta:
        """
        Define the model and fields
        """
        model = User
        fields = ('username', 'email', 'password1', 'password2')
