# from django.test import TestCase
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APIClient
# from blog_post.models import BlogPost
# from user.models import CustomUser


# class TestBlogPost(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.user = CustomUser.objects.create(email='testuser@example.com',
#                                               password='testpassword')

#         self.blog_data = {
#             'title': 'Test Blog Post',
#             'content': 'Test Content',
#             'image': 'testimage',
#             'author': self.user.profile,
#             'tags': 'testtags',
#         }

#     def test_create_blogpost(self):
#         self.url = reverse('blog-create')
#         self.assertTrue(self.user.is_authenticated)
#         response = self.client.post(self.url, self.blog_data)

#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(BlogPost.objects.count(), 1)

#     def test_view_blogposts(self):
#         self.url = reverse('blog-view-all')
#         response = self.client.get(self.url)

#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_delete_blogpost(self):
#         self.client.force_login(self.user)
#         blog = BlogPost.objects.create(**self.blog_data)
#         blog_id = blog.id
#         self.url = reverse('blog-delete', args=(blog_id,))
#         response = self.client.delete(self.url)

#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(blog.objects.count(), 0)

#     def test_view_blog(self):
#         blog = BlogPost.objects.create(**self.blog_data)
#         url = reverse('blog-view', args=(blog.id,))

#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
