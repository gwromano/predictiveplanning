"""
Django settings for gettingstarted project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
#import django_heroku

#from decouple import gettingstarted

import gettingstarted
import boto3
from botocore.exceptions import NoCredentialsError

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "tWR6D;Lnjporc%$~M!hOkjKfZ!<m?t&_<fyOT$T)^mL-^pR;%[mSC|UhFxN"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # local apps
    "hello",
    # 3rd party apps
    "rest_framework",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "gettingstarted.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        #'DIRS': [BASE_DIR / "templates"],
        'DIRS': ["hello/templates"],
        #"DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "gettingstarted.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE" : "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3")
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

AUTHENTICATION_BACKENDS = (
    ('django.contrib.auth.backends.ModelBackend'),
)


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Amazon S3 Settings
# AWS_ACCESS_KEY_ID = gettingstarted('AWS_ACCESS_KEY_ID')

# AWS_SECRET_ACCESS_KEY = gettingstarted('AWS_SECRET_ACCESS_KEY')

# AWS_STORAGE_BUCKET_NAME = gettingstarted('AWS_STORAGE_BUCKET_NAME')
 
# AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

# AWS_DEFAULT_ACL = 'public-read'

# AWS_S3_OBJECT_PARAMETERS = {
#     'CacheControl': 'max-age=86400'
# }

# AWS_LOCATION = 'static'

# AWS_QUERYSTRING_AUTH = False

# AWS_HEADERS = {
#     'Access-Control-Allow-Origin': '*',
# }

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'

# STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'

# MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'

# amazon s3 settings
AWS_ACCESS_KEY_ID = 'AKIASVQ2RXGK3KPWDYFF'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'predplanning2'
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_REGION_NAME = 'us-east-1'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_VERIFY = True
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage' 

# uploading
# def upload_to_aws(local_file, bucket, s3_file):
#     s3 = boto3.client('s3', aws_access_key_id='AKIASVQ2RXGK3KPWDYFF',
#                       aws_secret_access_key='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')

#     try:
#         s3.upload_file(local_file, bucket, s3_file)
#         print("Upload Successful")
#         return True
#     except FileNotFoundError:
#         print("The file was not found")
#         return False
#     except NoCredentialsError:
#         print("Credentials not available")
#         return False


# uploaded = upload_to_aws('local_file', 'bucket_name', 's3_file_name')


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = "/static/"

# django_project/settings.py
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"  

#django_heroku.settings(locals())
