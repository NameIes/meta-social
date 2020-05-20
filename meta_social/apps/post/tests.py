from django.contrib.auth.models import User
from django.test import TestCase, Client


class MetaSetUp(TestCase):
    fixtures = ["test_db.json"]

    def setUp(self):
        self.client = Client()
        self.user = User.objects.get(username="test_user")
        self.client.force_login(user=self.user)


class PostView(MetaSetUp):
    def setUp(self):
        super().setUp()
        self.response = self.client.get('/post/1/')

    def test_page(self):
        self.assertEqual(self.response.status_code, 200)
