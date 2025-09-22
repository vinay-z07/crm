from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Add to INSTALLED_APPS
INSTALLED_APPS = [
    # Add your default Django apps here, for example:
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Custom and third-party apps
    "apps.users",
    "rest_framework",
    "rest_framework_simplejwt",
]

DEBUG = True
AUTH_USER_MODEL = "users.User"
# This email address will be used as the default sender for outgoing emails.
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

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

SECRET_KEY = "django-insecure-CHANGE_THIS_TO_A_RANDOM_SECRET_KEY"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "apps" / "users" / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "crm_mt",
        "USER": "root",
        "PASSWORD": "",
        "HOST": "localhost",  # Or your MySQL server address
        "PORT": "3306",       # Default MySQL port
    }
}

STATIC_URL = "/static/"

ROOT_URLCONF = "config.urls"

# To install djangorestframework-simplejwt, run the following command in your terminal:
# pip install djangorestframework-simplejwt

#python manage.py makemigrations
#python manage.py migrate
#python manage.py runserver
