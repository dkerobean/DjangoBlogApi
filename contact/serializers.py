from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("Email field is required")
        return value
