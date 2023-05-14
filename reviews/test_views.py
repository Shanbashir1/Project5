from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def test_get_addreview(self):
        response = self.client.get("/add_review")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_get_editreview(self):
        response = self.client.get("/edit_review")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_get_delete_review(self):
        response = self.client.get("/delete_review")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
