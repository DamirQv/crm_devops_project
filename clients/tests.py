from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from .models import Client

class ClientTest(TestCase):
    def test_create_client(self):
        client = Client.objects.create(
            name="Test",
            email="test@mail.com",
            phone="123"
        )
        self.assertEqual(client.name, "Test")