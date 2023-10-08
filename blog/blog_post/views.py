from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Tag, Category
from .serializers import TagSerializer, CategorySerializer
from rest_framework.permissions import IsAdminUser # noqa


class TagCreateView(APIView):

    def get(self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class TagDetailView(APIView):

    # permission_classes = [IsAdminUser]

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

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

