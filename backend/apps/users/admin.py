# backend/apps/users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User, Department

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "created_at")
    search_fields = ("name", "code")

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal", {"fields": ("first_name", "last_name", "email", "phone", "avatar")}),
        ("Company", {"fields": ("department", "designation", "role")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups")}),
        ("MFA/Email", {"fields": ("mfa_enabled", "email_verified")}),
    )
    list_display = ("username", "email", "first_name", "last_name", "role", "department", "is_active")
    search_fields = ("username", "email", "first_name", "last_name")
