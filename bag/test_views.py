from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def test_view_bag(self):
        response = self.client.get("/view_bag")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_add_to_bag(self):
        response = self.client.get("/add_to_bag")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_adjust_bag(self):
        response = self.client.get("/adjust_bag")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_remove_from_bag(self):
        response = self.client.get("/adjust_bag")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
