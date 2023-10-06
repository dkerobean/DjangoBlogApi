from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Tag
from .serializers import TagSerializer
from rest_framework.permissions import IsAdminUser


class TagCreateView(APIView):

    def get(self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class TagDetailView(APIView):

    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_404_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            tag = Tag.objects.get(id=pk)
            tag.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Tag.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
