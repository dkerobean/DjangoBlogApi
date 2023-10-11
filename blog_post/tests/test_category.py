from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from blog_post.models import Category
from user.models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken


class TestCategories(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.contact_data = {
            'name': 'TestCategory',
        }
        self.user = CustomUser.objects.create_user(email='testuser@example.com', password='testpassword') # noqa

        # Generate a JWT token for the user
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)

    def test_category_view(self):
        self.url = reverse('category-list')
        response = self.client.get(self.url, self.contact_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_category_create(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}') # noqa

        self.url = reverse('category-create')
        response = self.client.post(self.url, self.contact_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)

    def test_category_delete(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}') # noqa

        category = Category.objects.create(**self.contact_data)
        url = reverse('category-delete', kwargs={'pk': category.id})

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 0)
