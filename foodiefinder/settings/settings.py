"""
Django settings for foodiefinder project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-dy966h_k$)(6^8iwu-66ul)e--g80wpk*7s5u1u35b!@!%ixra'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Default to development
ENVIRONMENT = os.getenv('DJANGO_ENV', 'development')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'login',
    'account',
    'food'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# REST_FRAMEWORK = {
#         'DEFAULT_AUTHENTICATION_CLASSES': [
#             'django_cognito_jwt.JSONWebTokenAuthentication',
#     ],
# }

ROOT_URLCONF = 'foodiefinder.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'foodiefinder.wsgi.application'


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

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'assets')
]
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_URL = 'log_in_user'
LOGOUT_URL = 'log_out_user'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# AWS Cognito
AWS_COGNITO_USER_POOL_ID = 'us-east-1_5dDseufsr'
AWS_COGNITO_APP_CLIENT_ID = '2mfaa2po88die806iapdpi7vfu'
AWS_COGNITO_APP_CLIENT_SECRET = 'hav0qn61pn2c7g5unibmhie69tt2g2asv2kjbb56tpr6l01pdvk'  # if applicable
AWS_COGNITO_REGION = 'us-east-1'
AWS_COGNITO_URL = f'https://foodiefinder.auth.{AWS_COGNITO_REGION}.amazoncognito.com'
if ENVIRONMENT == 'production':
    AWS_COGNITO_LOGIN_REDIRECT_URL = 'http://localhost:8080/callback'  # Update this to your callback URL
    AWS_COGNITO_LOGOUT_REDIRECT_URL = 'http://localhost:8080/'
else:
    AWS_COGNITO_LOGIN_REDIRECT_URL = 'http://localhost:8000/callback'  # Update this to your callback URL
    AWS_COGNITO_LOGOUT_REDIRECT_URL = 'http://localhost:8000/'

