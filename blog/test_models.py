from django.test import TestCase
from blog.models import Post, Category


class TestPostModel(TestCase):
    """
    Test if the input fields specified in the Post model
    returns correct data
    """
    def test_should_return_post_title(self):
        post = Post(title='title')
        self.assertEqual(str(post), 'title')


class TestCathegoryModel(TestCase):
    """
    Test the Category model
    if it does return the correct data
    """
    def test_should_return_cat_name(self):
        cat = Category(name='name')
        self.assertEqual(str(cat), 'name')
