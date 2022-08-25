"""
Contains functions to test the application
"""
from django.test import TestCase
from django.contrib.auth.models import User
from .forms import SignUpForm


class LogInTest(TestCase):
    """
    Test the login form
    """
    def setUp(self):
        """
        Use the mockup data
        """
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        """
        Send login data
        """
        response = self.client.post('/members/login/', self.credentials,
                                    follow=True)
        self.assertTrue(response.context['user'].is_authenticated)


class TestRegisterForm(TestCase):
    """
    Test the register form
    """
    def test_item_username_is_requied(self):
        """
        Check if the username field is required
        and if the user is notified about it while
        trying to submit the form with this input field empty
        """
        form = SignUpForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors.keys())
        self.assertEqual(form.errors['username'][0], 'This field is required.')

    def test_item_email_is_requied(self):
        """
        Check if the email field is required
        and if the user is notified about it while
        trying to submit the form with this input field empty
        """
        form = SignUpForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_item_password1_is_requied(self):
        """
        Check if the password1 field is required
        and if the user is notified about it while
        trying to submit the form with this input field empty
        """
        form = SignUpForm({'password1': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('password1', form.errors.keys())
        self.assertEqual(form.errors['password1'][0],
                         'This field is required.')

    def test_item_password2_is_requied(self):
        """
        Check if the password2 field is required
        and if the user is notified about it while
        trying to submit the form with this input field empty
        """
        form = SignUpForm({'password2': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors.keys())
        self.assertEqual(form.errors['password2'][0],
                         'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Check if all the meta tags match
        naming used in the Form
        """
        form = SignUpForm()
        self.assertEqual(form.Meta.fields, ('username', 'email', 'password1',
                                            'password2', 'agree'))
