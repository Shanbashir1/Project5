from django.contrib import admin
from .models import Category, Product
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Class to access the Category model via Django Admin panel
    """
    list_display = (
     'friendly_name',
     'name',
    )


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    """
    Class to access the Products model via Django Admin panel
    """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
        'gender',
        'in_stock',
    )
    search_fields = (
        'category__name', 'name',
        'rating',)

    summernote_fields = "description, features"
    ordering = ('sku',)
