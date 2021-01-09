from rest_framework import serializers


class UserUpdateSerializer(serializers.Serializer):
    name = serializers.CharField()
    job = serializers.CharField()


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
