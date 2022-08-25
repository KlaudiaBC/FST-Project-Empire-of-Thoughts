from django.test import TestCase
from blog.models import Post, Category


class TestPostModel(TestCase):
    def test_should_return_post_title(self):
        post = Post(title='title')
        self.assertEqual(str(post), 'title')


class TestCathegoryModel(TestCase):
    def test_should_return_cat_name(self):
        cat = Category(name='name')
        self.assertEqual(str(cat), 'name')
