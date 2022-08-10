from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    model = Post
    queryset = Post.objects.order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostView(DetailView):
    model = Post
    template_name = "post_view.html"
