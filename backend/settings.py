# Add to INSTALLED_APPS
INSTALLED_APPS += [
    "apps.users",
    "rest_framework",
    "rest_framework_simplejwt",
]

AUTH_USER_MODEL = "apps.users.User"
DEFAULT_FROM_EMAIL = "no-reply@yourdomain.com"

# Simple JWT
from datetime import timedelta
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=4),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
}

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
}
