from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Post

class PostForm(forms.ModelForm):
    """
    Form for editing a blog post
    """
    class Meta:
        model = Post
        widgets = {
            'body': SummernoteWidget()
        }
        fields = [
            'title',
            'slug',
            'body',
            'image',
        ]

class AddPostForm(forms.ModelForm):
    """
    Form for adding a blog post
    """
    class Meta:
        model = Post
        widgets = {
            'body': SummernoteWidget()
        }

        fields = [
            'title',
            'slug',
            'body',
            'image',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
