from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def test_get_all_product(self):
        response = self.client.get("/product")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_get_product_detail(self):
        response = self.client.get("/product")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_get_add_product(self):
        response = self.client.get("/product")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_get_edit_product(self):
        response = self.client.get("/product")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_get_delete_product(self):
        response = self.client.get("/product")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
