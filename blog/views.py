"""
Define and customise Views
"""
from django.views.generic import ListView, DetailView, CreateView, \
    UpdateView, DeleteView
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .models import Post, Comment, Category
from .forms import PostForm, CommentForm


class PostList(ListView):
    """
    Define attributes for the list of published posts
    which will render in specyfied html file.
    """
    model = Post
    queryset = Post.objects.order_by("-created_on")
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostList, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


class PostView(DetailView):
    """
    Define attributes for the detalic view of the post,
    which will render in specyfied html file.
    """
    model = Post
    template_name = 'post_view.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        sum_likes = stuff.sum_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["sum_likes"] = sum_likes
        context["liked"] = liked

        return context


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


def CategoryList(request, cats):
    category_post = Post.objects.filter(category=cats)
    return render(request, 'categories.html', {
        'cats': cats.title, 'category_post': category_post})


def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'categories_list.html', {
        'cat_menu_list': cat_menu_list})


def LikeClick(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('post_view', args=[str(pk)]))


class AddComment(CreateView):
    """
    Define attributes for the detalic view of the post,
    which will render in specyfied html file.
    """
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
