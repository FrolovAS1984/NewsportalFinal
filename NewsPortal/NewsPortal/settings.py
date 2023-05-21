"""
Django settings for NewsPortal project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

from .secret_doc import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(lc^v5@1zd$(d)4v3^ot5z=*tdghk--ry_=(=k!&ccot=48+uk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'fpages',
    'django_filters',
    'news.apps.NewsConfig',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',
    'django_apscheduler',

]

SITE_ID = 1

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'news.middlewares.TimezoneMiddleware',

]

ROOT_URLCONF = 'NewsPortal.urls'

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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'NewsPortal.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

LANGUAGES = [('en-us', 'English'), ('ru', 'Russian')]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]
LOGIN_REDIRECT_URL = "/posts"

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

SITE_URL = 'http://127.0.0.1:8000'

ACCOUNT_FORMS = {"signup": "accounts.forms.CustomSignupForm"}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = news_EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = news_EMAIL_HOST_PASSWORD
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = news_DEFAULT_FROM_EMAIL

EMAIL_SUBJECT_PREFIX = ''
SERVER_EMAIL = news_SERVER_EMAIL

APSCHEDULER_DATETIME = 'N j, Y, f:s a'
APSCHEDULER_RUN_NOW_TIMEOUT = 25

# __________________________________________________________________________________________
ADMINS = (
    (news_login, news_mail),
)

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'style': '{',
#     'formatters': {
#         'console_formatter_DEBUG': {
#             'format': '{asctime} [{levelname}] - {message}',
#             'datetime': '%m.%d %H:%M:%S',
#             'style': '{',
#         },
#         'console_formatter_WARNING': {
#             'format': '{asctime} [{levelname}]- {message} {pathname}',
#             'datetime': '%m.%d %H:%M:%S',
#             'style': '{',
#         },
#         'console_formatter_ERROR': {
#             'format': '{asctime} [{levelname}] - {message} {pathname} {exc_info}',
#             'datetime': '%m.%d %H:%M:%S',
#             'style': '{',
#         },
#         'file_formatter_general': {
#             'format': '{asctime} [{levelname}] {module} - {message}',
#             'datetime': '%m.%d %H:%M:%S',
#             'style': '{',
#         },
#         'file_formatter_errors': {
#             'format': '{asctime} [{levelname}] - {message} {pathname} {exc_info}',
#             'datetime': '%m.%d %H:%M:%S',
#             'style': '{',
#         },
#         'file_formatter_security': {
#             'format': '{asctime} [{levelname}] {module} - {message}',
#             'datetime': '%m.%d %H:%M:%S',
#             'style': '{',
#         },
#         'mail_formatter': {
#             'format': '{asctime} [{levelname}] - {message} {pathname}',
#             'datetime': '%m.%d %H:%M:%S',
#             'style': '{',
#         },
#
#     },
#     'filters': {
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue',
#         },
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse',
#         },
#     },
#     'handlers': {
#         'console_handler_DEBUG': {
#             'level': 'DEBUG',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'console_formatter_DEBUG'
#         },
#         'console_handler_WARNING': {
#             'level': 'WARNING',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'console_formatter_WARNING'
#         },
#         'console_handler_ERROR': {
#             'level': 'ERROR',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'console_formatter_ERROR'
#         },
#         'file_handler_general': {
#             'level': 'INFO',
#             'filters': ['require_debug_false'],
#             'class': 'logging.FileHandler',
#             'filename': 'general.log',
#             'formatter': 'file_formatter_general',
#         },
#         'file_handler_errors': {
#             'level': 'ERROR',
#             'class': 'logging.FileHandler',
#             'filename': 'errors.log',
#             'formatter': 'file_formatter_errors',
#         },
#         'file_handler_security': {
#             'level': 'INFO',
#             'class': 'logging.FileHandler',
#             'filename': 'security.log',
#             'formatter': 'file_formatter_security',
#         },
#         'mail_admins_handler': {
#             'level': 'ERROR',
#             'filters': ['require_debug_false'],
#             'class': 'django.utils.log.AdminEmailHandler',
#             'formatter': 'mail_formatter',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console_handler_DEBUG',
#                          'console_handler_WARNING',
#                          'console_handler_ERROR',
#                          'file_handler_general'
#                          ],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#         'django.request': {
#             'handlers': ['file_handler_errors',
#                          'mail_admins_handler'
#                          ],
#             'level': 'ERROR',
#             'propagate': False,
#         },
#         'django.server': {
#             'handlers': ['file_handler_errors',
#                          'mail_admins_handler'
#                          ],
#             'level': 'ERROR',
#             'propagate': False,
#         },
#         'django.template': {
#             'handlers': ['file_handler_errors'],
#             'level': 'ERROR',
#             'propagate': False,
#         },
#         'django.db.backends': {
#             'handlers': ['file_handler_errors'],
#             'level': 'ERROR',
#             'propagate': False,
#         },
#         'django.security': {
#             'handlers': ['file_handler_security'],
#             'level': 'INFO',
#             'propagate': False,
#         }
#     }
# }
