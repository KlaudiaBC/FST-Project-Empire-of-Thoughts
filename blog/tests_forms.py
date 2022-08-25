"""
Contains functions to test the application
"""
from django.test import TestCase
from .forms import PostForm, CommentForm


class TestPostForm(TestCase):
    """
    Test the Post form
    """
    def test_item_title_is_requied(self):
        """
        Check if the title input
        in the Post form is required
        """
        form = PostForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_item_category_is_requied(self):
        """
        Check if the category input
        in the Post form is required
        """
        form = PostForm({'category': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('category', form.errors.keys())
        self.assertEqual(form.errors['category'][0], 'This field is required.')

    def test_item_author_is_requied(self):
        """
        Check if the author input
        in the Post form is required
        """
        form = PostForm({'author': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('author', form.errors.keys())
        self.assertEqual(form.errors['author'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Check if the names in meta class match
        to the PostForm objects names
        """
        form = PostForm()
        self.assertEqual(form.Meta.fields, ('title', 'category', 'body',
                                            'author',))


class TestCommentForm(TestCase):
    """
    Test the Comment form
    """
    def test_item_body_is_requied(self):
        """
        Check if the body input
        in the Comment form is required
        """
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_item_name_is_requied(self):
        """
        Check if the name input
        in the Comment form is required
        """
        form = CommentForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Check if the names in meta class match
        to the CommentForm objects names
        """
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ('body', 'name'))
