from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Tag


class TestTag(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.tag_data = {
            'name': 'TestTag'
        }

    def test_tag_create(self):
        self.url = reverse('tag-create')
        response = self.client.post(self.url, self.tag_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tag.objects.count(), 1)

    def test_tag_get(self):
        tag = Tag.objects.create(**self.tag_data)
        url = reverse('tag-get', kwargs={'pk': tag.id})

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_tag_delete(self):
        tag = Tag.objects.create(**self.tag_data)
        url = reverse('tag-delete', kwargs={'pk': tag.id})

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Tag.objects.count(), 0)
