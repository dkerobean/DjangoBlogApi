from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from blog_post.models import Tag
from user.models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken


class TestTag(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.tag_data = {
            'name': 'TestTag'
        }
        self.user = CustomUser.objects.create_user(email='test@example', password='testpassword') # noqa

        # Generate a JWT token for the user
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)

    def test_tag_create(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}') # noqa

        self.url = reverse('tag-create')
        response = self.client.post(self.url, self.tag_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tag.objects.count(), 1)

    def test_tag_view(self):
        self.url = reverse('tag-list')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_tag_get(self):
    #     tag = Tag.objects.create(**self.tag_data)
    #     url = reverse('tag-get', kwargs={'pk': tag.id})

    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_tag_delete(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}') # noqa

        tag = Tag.objects.create(**self.tag_data)
        url = reverse('tag-delete', kwargs={'pk': tag.id})

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Tag.objects.count(), 0)
