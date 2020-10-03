from django.test import TestCase
from rest_framework.test import APIClient
# Create your tests here.
from rest_framework.test import RequestsClient

class HomeTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_home_works(self):

        response = self.client.get('')

        self.assertEqual(response.status_code, 200)
