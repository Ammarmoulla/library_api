from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Post

# Create your tests here.

class PostTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(
            username="testuser",
            email="test@gmail.com",
            password="secret",
        )

        cls.post = Post.objects.create(
            title="test 1st post",
            body="this is test dont worry",
            author=cls.user
        )
    def test_post_model(self):
        self.assertEqual(self.post.title, "test 1st post")
        self.assertEqual(self.post.body, "this is test dont worry")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "test 1st post")
