from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    published = models.IntegerField(choices=STATUS, default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

