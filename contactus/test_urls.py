from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import ContactUs


class Test_Urls(SimpleTestCase):

    def test_contactus_url_is_resolved(self):
        url = reverse('contactus')
        self.assertEquals(resolve(url).func.view_class, ContactUs)
