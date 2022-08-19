"""
Define and customise Models
"""
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    Define the Post model
    """
    title = models.CharField(max_length=200)
    body = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    published = models.IntegerField(choices=STATUS, default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="blog_posts")
    likes = models.ManyToManyField(User, related_name="likes")
    category = models.CharField(max_length=100, default='motivation')

    class Meta:
        """
        Set the order of displaying the posts
        """
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def sum_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        """
        Function allows to redirect the User
        back to the home page
        """
        return reverse('home')


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Function allows to redirect the User
        back to the home page
        """
        return reverse('home')


class Comment(models.Model):
    """
    Define the Comment model
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="blog_comments"
    )
    name = models.CharField(max_length=100)
    body = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Set the order of displaying the posts
        """
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
