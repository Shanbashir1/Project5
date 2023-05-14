from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import AddReview


class Test_Urls(SimpleTestCase):

    def test_addreview_url_is_resolved(self):
        url = reverse('add_review')
        self.assertEquals(resolve(url).func.view_class, AddReview)
