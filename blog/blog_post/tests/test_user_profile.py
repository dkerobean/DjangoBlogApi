from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from blog_post.models import UserProfile
from user.models import CustomUser


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

    def test_create_user_profile(self):
        self.url = reverse('profile-create')
        response = self.client.post(self.url, self.user_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserProfile.objects.count(), 1)
