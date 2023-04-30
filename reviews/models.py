from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Reviews(models.Model):
    """
    Model for Reviews
    """

    
    class Meta:
        verbose_name_plural = "Reviews"


    title = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=25)
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
    rating = models.TextField(max_length=200, null=True)
    customer_review = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    approved = models.BooleanField(default=False)


    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.name
