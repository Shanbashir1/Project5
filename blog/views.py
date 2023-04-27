from django.shortcuts import render
from . import views
from .models import Post, Comment


def post_list(request):
    """View to post a blog"""
    post_list = Post.objects.all()

    return render(request, 'blog/blog.html')
