from django.contrib import admin
from .models import ContactModel


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',  'email', 'subject', 'created_on')
    search_fields = ('first_name', 'last_name',)
    list_filter = ('first_name', 'last_name',  'email')
