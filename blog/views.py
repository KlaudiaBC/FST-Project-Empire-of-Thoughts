"""
Define and customise Views
"""
from django.views.generic import ListView, DetailView, CreateView, \
    UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import PostForm
from .forms import CommentForm


class PostList(ListView):
    """
    Define attributes for the list of published posts
    which will render in specyfied html file.
    """
    model = Post
    queryset = Post.objects.order_by("-created_on")
    template_name = "index.html"


class PostView(DetailView):
    """
    Define attributes for the detalic view of the post,
    which will render in specyfied html file.
    """
    model = Post
    template_name = 'post_view.html'


class AddPost(CreateView):
    """
    Define attributes for the Add Post form,
    which will render in specyfied html file.
    """
    model = Post
    form_class = PostForm
    template_name = "add_post.html"


class UpdatePost(UpdateView):
    """
    Define attributes for the Edit Post form,
    which will render in specyfied html file.
    """
    model = Post
    form_class = PostForm
    template_name = "update_post.html"


class DeletePost(DeleteView):
    """
    Define attributes for the delete post page,
    which will render in specyfied html file.
    """
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('home')


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post_view', args=[str(pk)]))


class AddComment(CreateView):
    """
    Define attributes for the detalic view of the post,
    which will render in specyfied html file.
    """
    model = Comment
    form_class = CommentForm
    fields = "__all__"
    template_name = 'add_comment.html'