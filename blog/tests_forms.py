"""
Contains functions to test the application
"""
from django.test import TestCase
from .forms import PostForm, CommentForm


class TestPostForm(TestCase):

    def test_item_title_is_requied(self):
        form = PostForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_item_category_is_requied(self):
        form = PostForm({'category': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('category', form.errors.keys())
        self.assertEqual(form.errors['category'][0], 'This field is required.')
        
    def test_item_author_is_requied(self):
        form = PostForm({'author': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('author', form.errors.keys())
        self.assertEqual(form.errors['author'][0], 'This field is required.')
        
    def test_fields_are_explicit_in_form_metaclass(self):
        form = PostForm()
        self.assertEqual(form.Meta.fields, ('title', 'category', 'body',
                                            'author',))


class TestCommentForm(TestCase):

    def test_item_body_is_requied(self):
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_item_name_is_requied(self):
        form = CommentForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')
        
    def test_fields_are_explicit_in_form_metaclass(self):
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ('body', 'name'))
