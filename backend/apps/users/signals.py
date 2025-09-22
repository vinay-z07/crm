# backend/apps/users/signals.py
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import User
from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save, sender=User)
def welcome_on_create(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject="Welcome to CRM",
            message=f"Hello {instance.first_name or instance.username}, your account has been created.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[instance.email],
            fail_silently=True,
        )
