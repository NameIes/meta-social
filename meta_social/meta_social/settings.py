"""
Django settings for meta_social project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os, sys

# Simple changing DB and redis

START_WITH_DOCKER = False

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

APPS_DIR = os.path.join(BASE_DIR, 'apps/')
sys.path.insert(0, APPS_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#bhq1g66br=mwyxcvxxc+1yu=1fq@wcv--ys&&7=233@0^zv5!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = not START_WITH_DOCKER

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    'chat.apps.ChatConfig',
    'community.apps.CommunityConfig',
    'core.apps.CoreConfig',
    'friends.apps.FriendsConfig',
    'music.apps.MusicConfig',
    'post.apps.PostConfig',
    'user_profile.apps.UserProfileConfig',

    'crispy_forms',
    'django_countries',
    'channels',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.vk',
    'allauth.socialaccount.providers.facebook',
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

ROOT_URLCONF = 'meta_social.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(APPS_DIR, 'chat/templates'),
            os.path.join(APPS_DIR, 'community/templates'),
            os.path.join(APPS_DIR, 'core/templates'),
            os.path.join(APPS_DIR, 'friends/templates'),
            os.path.join(APPS_DIR, 'music/templates'),
            os.path.join(APPS_DIR, 'post/templates'),
            os.path.join(APPS_DIR, 'user_profile/templates'),
        ],
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

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 4

WSGI_APPLICATION = 'meta_social.wsgi.application'
ASGI_APPLICATION = 'meta_social.routing.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('redis' if START_WITH_DOCKER else '127.0.0.1', 6379)],
        },
    },
}

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

if START_WITH_DOCKER:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'DB',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': 'db',
            'PORT': '5432',
        },
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        },
    }

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'

LOGOUT_URL = '/accounts/logout/'
LOGOUT_REDIRECT_URL = '/accounts/login/'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'collectedstatic')

CRISPY_TEMPLATE_PACK = 'bootstrap4'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'piryazev555@gmail.com'
# EMAIL_HOST_PASSWORD = 'zelt gjfv bhtt zhlt'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

ACCOUNT_EMAIL_REQUIRED = True
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_FILE_STORAGE = "django_s3_storage.storage.S3Storage"

AWS_REGION = "nl-ams"
AWS_ACCESS_KEY_ID = "SCW4Y1H2449R5QJ05B52"
AWS_SECRET_ACCESS_KEY = "88aed883-f609-4331-b728-69b866fca6a2"
AWS_S3_ENDPOINT_URL = "https://s3.nl-ams.scw.cloud"
AWS_S3_BUCKET_NAME = "social-bucket"

if START_WITH_DOCKER:
    AWS_REGION_STATIC = "nl-ams"
    AWS_ACCESS_KEY_ID_STATIC = "SCW4Y1H2449R5QJ05B52"
    AWS_SECRET_ACCESS_KEY_STATIC = "88aed883-f609-4331-b728-69b866fca6a2"
    AWS_S3_ENDPOINT_URL_STATIC = "https://s3.nl-ams.scw.cloud"
    AWS_S3_BUCKET_NAME_STATIC = "social-static"
    STATICFILES_STORAGE = 'django_s3_storage.storage.StaticS3Storage'

FIXTURE_DIRS = [
    'core/fixtures',
    'user_profile/fixtures',
]
