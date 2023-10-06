from rest_framework import serializers
from .models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Name must be specified")
        return value
