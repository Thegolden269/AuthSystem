from rest_framework import serializers
from .models import CustomUser
from utils.validators import (
    validate_email,
    validate_password,
    validate_first_name,
    validate_last_name,
)


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'password']
        read_only_fields = ['id']

    def validate_email(self, value):
        validate_email(value)
        return value

    def validate_password(self, value):
        validate_password(value)
        return value

    def validate_first_name(self, value):
        validate_first_name(value)
        return value

    def validate_last_name(self, value):
        validate_last_name(value)
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)  # Django hashing
        user.save()
        return user
