from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from user.models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken


class TestUserProfile(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create(email='testuser@example.com',
                                              password='testpassword')
        self.user_data = {
            'user': self.user,
            'name': 'test_name',
            'position': 'test_position',
            'bio': 'test_bio',
            'profile_picture': 'test_profile_picture',
            'website': 'www.example.com',
            'github': 'www.github.com',
            'linkedin': 'www.linkedin.com',
            }

        # Generate a JWT token for the user
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)

    def test_view_users_profiles(self):
        self.url = reverse('profiles')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_user_profile(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}') # noqa

        pk = self.user.id
        self.url = reverse('profile-view', args=(pk,))
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user'], self.user.id)

    def test_delete_profile(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}') # noqa

        pk = self.user.id
        self.url = reverse('profile-delete', args=(pk,))

        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
