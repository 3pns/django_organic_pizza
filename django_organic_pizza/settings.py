"""
Django settings for django_organic_pizza project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# configurable settings
ENV = os.getenv('DJANGO_ENV', 'development')
SECRET_KEY = os.getenv('DJANGO_ORGANIC_PIZZA_SECRET_KEY')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DJANGO_ORGANIC_PIZZA_DB_NAME'),
        'USER': os.getenv('DJANGO_ORGANIC_PIZZA_DB_USER'),
        'PASSWORD': os.getenv('DJANGO_ORGANIC_PIZZA_DB_PASSWORD'),
        'HOST': os.getenv('DJANGO_ORGANIC_PIZZA_DB_HOST', 'localhost'),
    },
}

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
if ENV == "production" : DEBUG = False

ALLOWED_HOSTS = ['localhost', '0.0.0.0']
if ENV == "production" : ALLOWED_HOSTS.append('DJANGO_ORGANIC_PIZZA_HOST')
# if ENV == "production" : STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_organic_pizza.apps.DjangoOrganicPizzaConfig',
]

if ENV != "production":
    INSTALLED_APPS.append('django_nose')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'django_organic_pizza.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'django_organic_pizza/templates'),
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

WSGI_APPLICATION = 'django_organic_pizza.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s][%(levelname)s][%(module)s][%(process)d][%(thread)d]: %(message)s'
        },
        'simple': {
            'format': '[%(asctime)s][%(levelname)s][%(module)s][%(funcName)s]: %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'filters': ['require_debug_false'],
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'filters': ['require_debug_true'],
        },
        'django.request': {
            'handlers': ['console'],
            'level': ("DEBUG") ,
            'propagate': False,
        },
        'django.server': {
            'handlers': ['console'],
            'level': ("DEBUG") ,
            'propagate': False,
        },
    },
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static") 
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "public"),
]


TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
