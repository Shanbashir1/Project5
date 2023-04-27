from django.shortcuts import render
from django.views.generic import ListView
from . import views
from .models import Post, Comment


class PostList(ListView):
    """A view to create the post on the blog page"""
    model = Post
    template_name = 'blog/blog.html'



def post_blog(request, slug):
    """ View to show posted blog"""

    post = Post.objects.filter(slug=slug).first()
    comments = Comment.objects.filter(blog_id=post)

    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, 'Action not allowed')
            return redirect(reverse('home'))
        else:
            user = request.user
            body = request.POST.get('body', '')
            comment = Comment(user=user, body=body, blog_id=post)
            comment.save()

    template = 'blog/post_blog.html'
    context = {
        'post': post,
        'comments': comments,
    }

    return render(request, template, context)

