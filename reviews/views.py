from django.shortcuts import render
from .models import Reviews
from .forms import ReviewsForm


def reviews(request):
    """
    Renders the reviews page
    """
    reviews_view = (
        Reviews.objects.all().filter(approved=True).order_by("-created_on"))
    return render(
        request,
        "reviews/reviews.html", {"reviews_view": reviews_view})
