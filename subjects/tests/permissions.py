from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class TestPermissions(APITestCase):

    def setUp(self) -> None:
        self.url_base = 'http://127.0.0.1:8000'
        self.user = User.objects.create(username='test')
        self.user.set_password('test')
        self.user.is_active = True
        self.user.save()
        self.token = self.client.post(f'{self.url_base}/api/token/', {
            'username': 'test',
            'password': 'test'
        })

    def test_retrieve(self):
        response = self.client.get(f'{self.url_base}/subjects/',
                                   HTTP_AUTHORIZATION=f'Bearer {self.token.data["access"]}')

        self.assertEqual(response.status_code, 200)

    def test_retrieve_fail(self):
        response = self.client.get(f'{self.url_base}/subjects/')

        self.assertEqual(response.status_code, 401)
