from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def test_get_contact(self):
        response = self.client.get("/contactus")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
