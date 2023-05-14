from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def test_get_post_blog(self):
        response = self.client.get("/post_blog")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_get_delete_comment(self):
        response = self.client.get("/delete_comment")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_get_editBlog(self):
        response = self.client.get("/edit_blog")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_get_editBlog(self):
        response = self.client.get("/edit_blog")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_get_deleteBlog(self):
        response = self.client.get("/delete_blog")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_get_PostLike(self):
        response = self.client.get("/post_blog")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_get_CommentLike(self):
        response = self.client.get("/post_blog")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
