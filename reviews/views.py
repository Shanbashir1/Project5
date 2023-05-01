from django.shortcuts import render
from .models import Reviews
from .forms import ReviewsForm
from django.views.generic import CreateView, UpdateView
from django.contrib import messages


def reviews(request):
    """
    Renders the reviews page
    """
    reviews_view = (
        Reviews.objects.all().filter(approved=True).order_by("-created_on"))
    return render(
        request,
        "reviews/reviews.html", {"reviews_view": reviews_view})

class AddReview(CreateView):
    """
    Allows the user to create a review. 
    """

    model = Reviews
    form_class = ReviewsForm
    template_name = "reviews/create_review.html"
    success_message = "Thank you for posting your review, your review is pending and awaiting approval!"

    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)


class EditReview(UpdateView):
    """
    Allows the user to edit the review
    """

    model = Reviews
    form_class = ReviewsForm
    template_name = "reviews/create_review.html"
    success_message = "Thank you the review has been updated successfully"