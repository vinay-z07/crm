# backend/apps/users/serializers.py
from rest_framework import serializers
from .models import User, Department
from django.contrib.auth.password_validation import validate_password

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ["id", "name", "code", "description", "created_at"]


class UserSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(), source="department", write_only=True, required=False
    )

    class Meta:
        model = User
        fields = [
            "id", "username", "email", "first_name", "last_name", "department", "department_id",
            "designation", "phone", "avatar", "role", "is_active", "mfa_enabled", "email_verified", "created_at"
        ]
        read_only_fields = ("email_verified", "created_at")


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    department_id = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), source="department")

    class Meta:
        model = User
        fields = ("username", "email", "password", "first_name", "last_name", "department_id", "designation", "phone")

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.is_active = False  # admin must enable or email verify
        user.save()
        return user
