from django.shortcuts import render, get_object_or_404, redirect
from .models import Reviews
from .forms import ReviewsForm
from django.views.generic import CreateView, UpdateView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def reviews(request):
    """
    Renders the reviews page
    """
    reviews_view = (
        Reviews.objects.all().filter(approved=True).order_by("-created_on"))
    return render(
        request,
        "reviews/reviews.html", {"reviews_view": reviews_view})


class AddReview(SuccessMessageMixin, CreateView):
    """
    Allows the user to create a review.
    """

    model = Reviews
    form_class = ReviewsForm
    template_name = "reviews/create_review.html"
    success_message = "Thank you for posting your review,\
         your review is pending and awaiting approval!"

    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)


class EditReview(SuccessMessageMixin, UpdateView):
    """
    Allows the user to edit the review
    """
    model = Reviews
    form_class = ReviewsForm
    template_name = "reviews/create_review.html"
    success_message = "Thank you the review has been updated successfully"


@login_required
def delete_review(SuccessMessageMixin, request, review_id):
    """
    Allows the use to delete the view
    """
    reviews = get_object_or_404(Reviews, id=review_id)
    reviews.delete()
    messages.success(request, "This review has been\
         deleted successfully")
    return redirect("reviews")
