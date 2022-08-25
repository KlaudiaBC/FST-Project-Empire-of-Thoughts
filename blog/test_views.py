"""
Contains functions to test the application
"""
from django.test import TestCase


class TestViews(TestCase):
    """
    Test the views
    """
    def test_get_post_list(self):
        """
        check if the post_list view render a correct template
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
