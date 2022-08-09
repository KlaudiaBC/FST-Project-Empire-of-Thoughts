from django.shortcuts import render
from .models import Post


def get_blog_one(request):
    post_list = Post.objects.all()
    context = {
        "posts": post_list
    }
    return render(request, 'blog/blog_one.html', context)
