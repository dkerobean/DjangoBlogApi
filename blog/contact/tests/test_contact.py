from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from contact.models import Contact


class ContactTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.contact_data = {
            'name': 'Test Name',
            'email': 'email@example.com',
            'message': 'Test Message'
        }

    def test_contact_get(self):
        self.url = reverse('contact-view')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_contact_create(self):
        self.url = reverse('contact-create')
        response = self.client.post(self.url, self.contact_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Contact.objects.count(), 1)
        self.assertTrue(Contact.objects.get().name, 'Test Name')
