from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


class PostList(ListView):
    model = Post
    queryset = Post.objects.order_by("-created_on")
    template_name = "index.html"


class PostView(DetailView):
    model = Post
    template_name = "post_view.html"


class AddPost(CreateView):
    model = Post
    template_name = "add_post.html"
    fields = "title", "body", "author"
