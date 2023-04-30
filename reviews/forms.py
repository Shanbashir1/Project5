from django import forms
from .models import Reviews


class ReviewsForm(forms.ModelForm):
    """
    Creates the Reviews form for the customer review page
    """

    class Meta:
        model = Reviews
        fields = ("title", "customer_review", "rating", "image")
