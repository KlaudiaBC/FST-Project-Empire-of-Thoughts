from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostView(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(published=1)
        post = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "post_view.html",
            {
                "post": post,
            },
        )
