# -*- coding: utf-8 -*-
"""Django settings for django-anysign demo project."""
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Configure some relative directories.
demoproject_dir = os.path.dirname(os.path.abspath(__file__))
demo_dir = os.path.dirname(demoproject_dir)
root_dir = os.path.dirname(demo_dir)
data_dir = os.path.join(root_dir, 'var')
cfg_dir = os.path.join(root_dir, 'etc')


# Mandatory settings.
ROOT_URLCONF = 'django_anysign_demo.urls'
WSGI_APPLICATION = 'django_anysign_demo.wsgi.application'


# Database.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Template.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
    },
]


# Required.
SECRET_KEY = "This is a secret made public on project's repository."

# Media and static files.
MEDIA_ROOT = os.path.join(data_dir, 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(data_dir, 'static')
STATIC_URL = '/static/'


# Applications.
INSTALLED_APPS = [
    # The actual django-anysign demo.
    'django_anysign_demo',
    # Standard Django applications.
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Stuff that must be at the end.
    'django_nose',
]


# BEGIN middlewares
MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
]
# END middlewares


# BEGIN settings.ANYSIGN.
ANYSIGN = {
    'BACKENDS': {
        'dummysign': 'django_dummysign.backend.DummySignBackend',
    },
    'SIGNATURE_TYPE_MODEL': 'django_anysign_demo.models.SignatureType',
    'SIGNATURE_MODEL': 'django_anysign_demo.models.Signature',
    'SIGNER_MODEL': 'django_anysign_demo.models.Signer',
}
# END settings.ANYSIGN.


# Test/development settings.
DEBUG = True
TEMPLATE_DEBUG = DEBUG
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = [
    '--all-modules',
    '--cover-package=django_anysign',
    '--cover-package=django_anysign_demo',
    '--cover-package=django_dummysign',
    '--exclude-dir=demo/django_anysign_demo/migrations',
    '--no-path-adjustment',
    '--nocapture',
    '--verbosity=2',
    '--with-coverage',
    '--with-doctest',
]
SOUTH_TESTS_MIGRATE = False


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'null': {
            'class': 'logging.NullHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django_anysign': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'django_anysign_demo': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'django_dummysign': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}
