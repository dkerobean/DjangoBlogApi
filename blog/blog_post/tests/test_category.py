from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from blog_post.models import Tag, Category


class TestCategories(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.contact_data = {
            'name': 'TestCategory',
        }

    def test_category_view(self):
        self.url = reverse('category-list')
        response = self.client.get(self.url, self.contact_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_category_create(self):
        self.url = reverse('category-create')
        response = self.client.post(self.url, self.contact_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
