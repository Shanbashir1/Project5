from django.urls import path, include
from . import views

# Url Patterns for Contacts Page
urlpatterns = [
    path('contactus/', views.ContactUs.as_view(), name='contactus'),
    path('aboutus/', views.AboutUs.as_view(), name='aboutus'),
]
