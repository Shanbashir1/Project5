from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views.generic import ListView
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PostForm, AddPostForm
from .models import Post, Comment


class PostList(ListView):
    """A view to show the post on the blog page"""
    model = Post
    template_name = 'blog/blog.html'
    paginate_by = 4


def post_blog(request, slug):
    """ A View to show posted blog"""

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
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        liked = True

    template = 'blog/post_blog.html'
    context = {
        'post': post,
        'comments': comments,
        "liked": liked,
    }

    return render(request, template, context)


@login_required
def delete_comment(request, comment_id):
    """
    A view to allow the admin is to delete the comments
    """
    if not request.user.is_superuser:
        messages.error(
            request, 'You are not authorised to perform this action!')
        return redirect(
            reverse('blog'))

    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    messages.success(request, 'This comment was removed!')
    return redirect(reverse('blog'))


@login_required
def editBlog(request, slug):
    """
    A view to allow the admin to edit blog posts
    """
    if not request.user.is_superuser:
        messages.error(
            request, 'You are not authorized to perform this action!')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        postForm = PostForm(request.POST, request.FILES, instance=post)
        if postForm.is_valid():
            postForm.save()
            messages.success(request, 'Successfully updated the post!')
            return redirect('blog')
        else:
            messages.error(request, 'Failed to update the post. \
                Please ensure the form is valid.')

    else:
        postForm = PostForm(instance=post)
        messages.info(
            request, f'You are currently in editing mode: {post.slug}')

    template = 'blog/edit_blog.html'
    context = {
        'postForm': postForm,
        'post': post,
    }

    return render(request, template, context)


@login_required
def deleteBlog(request, slug):
    """
    A view to allow the admin to delete posts
    """
    if not request.user.is_superuser:
        messages.error(
            request, 'You are not authorized to perform this action!!')
        return redirect(reverse('home'))

    post = get_object_or_404(BlogPost, slug=slug)
    post.delete()
    messages.success(request, 'The post was deleted!')
    return redirect(reverse('blog'))


@login_required
def addBlog(request):
    """
    A view to allow the admin only to add blog post
    """
    if not request.user.is_superuser:
        messages.error(
             request, 'You are not authorized to perform this action!!')
        return redirect(reverse('home'))

    template = 'blog/add_blog.html'

    form = AddPostForm(request.POST or None, request.FILES or None)

    context = {
         'form': form,
     }

    if request.method == "POST":
        form = AddPostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            messages.success(
                request, 'A new blog has been successfully added')
            return redirect('blog')
        else:
            messages.error(
                request, 'An error occurred. \
                    Please ensure the form is valid.')
    else:
        form = AddPostForm()

    return render(request, template, context)


class PostLike(View):
    """
    A view to allow the logged in user to like posts
    """
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_blog', args=[slug]))


class CommentLike(View):
    """
    A view to allow the logged in user to like comments
    """
    def post(self, request, comment_id, slug, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=comment_id)
        print(comment)
        if comment.likes.filter(id=request.user.id).exists():
            comment.likes.remove(request.user)
        else:
            comment.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_blog', args=[slug]))
