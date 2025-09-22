# backend/apps/users/views.py
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.urls import reverse
from .models import User, Department
from .serializers import UserSerializer, DepartmentSerializer, RegisterSerializer
from .permissions import IsAdmin, IsManagerOrAdmin, IsSelfOrAdmin
from django.core.mail import send_mail

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all().order_by("name")
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticated, IsManagerOrAdmin]  # admins & managers can manage

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-created_at")
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ("create", "register"):
            return [permissions.AllowAny()]
        if self.action in ("list", "destroy"):
            return [permissions.IsAuthenticated(), IsAdmin()]
        if self.action in ("partial_update", "update"):
            return [permissions.IsAuthenticated(), IsSelfOrAdmin()]
        return [permissions.IsAuthenticated()]

    @action(detail=False, methods=["post"], url_path="register", permission_classes=[permissions.AllowAny])
    def register(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # send verification email
        verify_url = request.build_absolute_uri(reverse("users:verify-email", args=[str(user.email_verification_token)]))
        send_mail(
            subject="Verify your email",
            message=f"Please verify your email by clicking: {verify_url}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            fail_silently=False,
        )
        return Response({"detail": "User created. Verify email to activate account."}, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["get"], url_path="me")
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

    @action(detail=False, methods=["get"], url_path="verify-email/(?P<token>[^/.]+)", permission_classes=[permissions.AllowAny])
    def verify_email(self, request, token=None):
        user = get_object_or_404(User, email_verification_token=token)
        user.email_verified = True
        user.is_active = True
        user.email_verification_token = None
        user.save()
        return Response({"detail": "Email verified. You can login now."})
