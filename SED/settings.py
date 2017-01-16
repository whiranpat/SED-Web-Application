"""
Django settings for SED project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

from django.core.urlresolvers import reverse_lazy
import os

LOGIN_URL = reverse_lazy('login')
LOGIN_REDIRECT_URL = reverse_lazy('index')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a1u4znl-=0+!lzr=iyctr^*rxatx&6f%^60@62wtlyj+$_ea0$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['www.sedteam.com','localhost','54.152.243.242', '54.236.255.148']

# AWS_ACCESS_KEY_ID = 'YOUR-ACCESS-KEY-ID'
# AWS_SECRET_ACCESS_KEY = 'YOUR-SECRET-ACCESS-KEY'

# EMAIL_BACKEND = 'django_ses.SESBackend'

EMAIL_HOST ='smtp.gmail.com'
EMAIL_HOST_USER = 'scoutengineeringdaytest@gmail.com'
EMAIL_HOST_PASSWORD = 'SEDPass123'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

'''
If using gmail, you will need to unlock captcha
google unlock captcha
'''

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sedUI',
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

ROOT_URLCONF = 'SED.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'SED.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

# DATABASES = {
#    'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'sed_database_test',
#         'USER': 'root',
#         'PASSWORD':'test',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }

DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'SED_Database',
        'USER': 'sed',
        'PASSWORD':'Pass1234',
        'HOST': 'sed-db.cqpg4rn4jalr.us-east-1.rds.amazonaws.com',
        'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

# PROJECT_DIR = os.path.dirname(__file__)
# STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
STATIC_URL = '/sedUI/static/'
# STATICFILES_DIRS = (os.path.join(PROJECT_DIR, 'staticfiles'),)
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'index'
