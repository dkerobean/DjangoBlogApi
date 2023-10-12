from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            user = CustomUser.objects.create_user(
                username=validated_data['username'],
                email=validated_data['email'],
                password=validated_data['password']
            )
            return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(username=email, password=password)

            if not user:
                raise serializers.ValidationError("Unable to log in with provided credentials.") # noqa
        else:
            raise serializers.ValidationError("Must include 'email' and 'password'.") # noqa

        data['user'] = user
        return data
