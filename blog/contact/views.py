from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import ContactSerializer
from .models import Contact
from rest_framework.permissions import IsAdminUser


class ContactListView(APIView):

    def get(self, request):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactDetailView(APIView):

    def get(self, request, pk):
        try:
            contacts = Contact.objects.get(id=pk)
            serializer = ContactSerializer(contacts)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Contact.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        self.permission_classes = [IsAdminUser]
        self.check_permissions(request)
        try:
            contact = Contact.objects.get(id=pk)
            contact.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Contact.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
