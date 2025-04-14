"""
Django settings for starterproject project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-f3pm&hh)6iv-v$&-23#4b($m-ijvkm+xp(c1ibb4eq53ch7ufy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    # 'hrm',
    'template',
    'template1',
    "phonenumber_field",
    'lmsfeatures',
    'cms',
    'filehandler',
    'solo',
    'landingpage',
    # 'phonebook',
    
    'books',
    'globalapp',
    'ckeditor',
    'users',
    'des',
    'drf_spectacular',
    'rest_framework_simplejwt',
    'rest_framework',
    "corsheaders",
    'wkhtmltopdf',
    'jazzmin',
    'django_filters',
    'django_seed',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'starterproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'template1/templates/template')],  # This must point to the templates directory
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'starterproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_URL = '/static/'
STATIC_ROOT = '/home/moonsgal/api.futeresdevs.com/static'

MEDIA_ROOT = os.path.join(BASE_DIR, 'upload')
MEDIA_URL = '/upload/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field


########################################################### Project WISE CUSTOM SETINGS ##########################################################
#Special settings
AUTH_USER_MODEL = 'users.Users'
#CORS ALLOW
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

#Rest Framework Settings
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 5,
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
}

#JWT Settings
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=2880),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
}


#Documentations Settings
SPECTACULAR_SETTINGS = {
    'TITLE': 'Admin API',
    'DESCRIPTION': 'Your project description',
    'VERSION': '0.0.2',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}
PHONENUMBER_DEFAULT_REGION = 'US'
### Email Settings
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
EMAIL_BACKEND = 'des.backends.ConfiguredEmailBackend'
#pdf config
import os

# Define the path to wkhtmltopdf executable
WKHTMLTOPDF_PATH = '/path/to/wkhtmltopdf'

# Add the path to wkhtmltopdf to the environment
os.environ["PATH"] += os.pathsep + os.path.dirname(WKHTMLTOPDF_PATH)
# def configure_email():
#     try:
#         from globalapp.models import EmailConfigure
#         email = EmailConfigure.objects.first()
#         print(email)
#         if email:
#             EMAIL_HOST = email.host
#             EMAIL_PORT = email.port
#             EMAIL_HOST_USER = email.user
#             EMAIL_HOST_PASSWORD = email.email_password
#         else:
#             EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
#             EMAIL_PORT = 587
#             EMAIL_HOST_USER = '212cac752f672b'
#             EMAIL_HOST_PASSWORD = 'a233b5d755921e'
#     except Exception as e:
#         # Handle exceptions
#         print("Error configuring email:", e)
#         EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
#         EMAIL_PORT = 587
#         EMAIL_HOST_USER = '212cac752f672b'
#         EMAIL_HOST_PASSWORD = 'a233b5d755921e'

# configure_email()


