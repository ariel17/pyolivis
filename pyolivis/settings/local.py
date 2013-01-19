#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Local project settings.
"""
__author__ = "Ariel Gerardo Ríos (ariel.gerardo.rios@gmail.com)"


from common import *
# from os import environ
# from urlparse import urlparse


DEBUG = True

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        # Or path to database file if using sqlite3.
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pyolivis',
        'USER': 'root',  # Not used with sqlite3.
        'PASSWORD': '',  # Not used with sqlite3.
        # Set to empty string for localhost. Not used with sqlite3.
        'HOST': '',
        # Set to empty string for default. Not used with sqlite3.
        'PORT': '',
    }
}

INSTALLED_APPS += (
    'django_extensions',
)

# Configuration for registration application

ACCOUNT_ACTIVATION_DAYS = 1

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'ariel.gerardo.rios@gmail.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
EMAIL_PORT = 587


# vim:ft=python ts=4 tw=80 cc=+1:
