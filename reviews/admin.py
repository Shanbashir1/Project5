from django.contrib import admin
from .models import Reviews


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    """
    Displays the Reviews in the admin panel
    """
    list_display = (
        "name",
        "title",
        "created_on",
        "customer_review",
        "rating",
        "approved",
    )
