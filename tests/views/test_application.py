from django_organic_pizza.views import application
from django.test import TestCase
from django.test import Client

class ApplicationTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
