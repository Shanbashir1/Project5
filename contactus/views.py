from django.contrib import messages
from django.views.generic.edit import FormView, CreateView, View
from django.http import HttpResponseRedirect, request
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from .forms import ContactForm
from .models import ContactModel

# Create your views here.


class ContactUs(CreateView):
    '''
    Sends back a message to users who fill out a contact form
    '''
    model = ContactModel
    template_name = 'contactus/contact.html'
    fields = '__all__'
    success_url = reverse_lazy('contactus')

    # Send data back to the admin page
    def form_valid(self, form):
        messages.success(
            self.request,
            "Thank you for contacting us, your feedback and comments \
        have been forwarded onto a member of our team who \
        will be contacting you shortly.")
        form.save()
        return super().form_valid(form)
