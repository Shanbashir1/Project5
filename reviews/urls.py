from django.urls import path
from . import views


"""url paths"""
urlpatterns = [
    path("", views.reviews, name="reviews"),
    path("add_review/", views.AddReview.as_view(), name="add_review"),
    path("edit_review/<int:pk>", views.EditReview.as_view(),
         name="edit_review"),
    path("delete_review/<int:review_id>", views.delete_review,
         name="delete_review"),
]
