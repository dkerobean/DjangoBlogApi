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

    def view_user_profile(self):
        # login user or create user 
        # check user profile and manke sure its the same user
        # assert true status code is returned
