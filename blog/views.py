from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm


class PostList(ListView):
    model = Post
    queryset = Post.objects.order_by("-created_on")
    template_name = "index.html"


class PostView(DetailView):
    model = Post
    template_name = "post_view.html"


class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"


class UpdatePost(UpdateView):
    model = Post
    template_name = "update.html"
    fields = ['title', 'body']
