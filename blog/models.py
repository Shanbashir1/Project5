from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    body = models.TextField()
    image = models.ImageField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    body = models.TextField()
    blog_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    dateTime = models.DateTimeField(default=now)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-dateTime']

    def __str__(self):
        return self.user.username + " Comment: " + self.body
