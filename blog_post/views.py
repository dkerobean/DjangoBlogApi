from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Tag, Category, UserProfile, BlogPost
from .serializers import (TagSerializer,
                          CategorySerializer,
                          UserProfileSerializer,
                          BlogPostSerializer)
from rest_framework.permissions import IsAuthenticated # noqa
from rest_framework.throttling import AnonRateThrottle


class TagCreateView(APIView):

    def get(self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class TagDetailView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            tag = Tag.objects.get(id=pk)
            tag.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Tag.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


""" CATEGIORY """


class CategoryListView(APIView):

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryDetailView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            category = Category.objects.get(id=pk)
            category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


""" USER PROFILE """


class UserProfileView(APIView):

    def get(self, request):
        profiles = UserProfile.objects.all()
        serializer = UserProfileSerializer(profiles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserProfileDetailView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, pk):

        user = request.user

        if int(pk) != user.id:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        try:
            profile = UserProfile.objects.get(user=user)
            serializer = UserProfileSerializer(profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except UserProfile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        user = request.user

        if int(pk) != user.id:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        try:
            profile = UserProfile.objects.get(user=user)
            profile.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except UserProfile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


""" Blog Post """


class BlogListView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        blogs = BlogPost.objects.all()
        serializer = BlogPostSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BlogDetailView(APIView):

    permission_classes = [IsAuthenticated]
    throttle_classes = [AnonRateThrottle]

    def get(self, request, pk):
        try:
            blog = BlogPost.objects.get(id=pk)
            serializer = BlogPostSerializer(blog)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except BlogPost.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        user = request.user

        try:
            blog = BlogPost.objects.get(id=pk)

            if blog.author == user:
                serializer = BlogPostSerializer(blog, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            raise PermissionError("You do not have permissions \
                                  to perform this action")

        except BlogPost.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        user = request.user

        try:
            blog = BlogPost.objects.get(id=pk)
            if blog.author == user:
                blog.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                raise PermissionError("You do not have permissions \
                                      to perform this action")
        except BlogPost.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
