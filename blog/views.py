from django.shortcuts import render


def get_blog_one(request):
    return render(request, 'blog/blog_one.html')
