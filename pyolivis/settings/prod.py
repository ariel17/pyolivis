#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Development project settings.
"""
__author__ = "Ariel Gerardo Ríos (ariel.gerardo.rios@gmail.com)"


from common import *
from os import environ
from urlparse import urlparse


DEBUG = True

if environ.has_key('DATABASE_URL'):
    url = urlparse(environ['DATABASE_URL'])
    DATABASES = {
        'default': {
            # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            # Or path to database file if using sqlite3.
            'ENGINE': 'django.db.backends.', 
            'NAME': '',                      
            'USER': '',  # Not used with sqlite3.
            'PASSWORD': '',  # Not used with sqlite3.
            'HOST': '',  # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',  # Set to empty string for default. Not used with sqlite3.
        }
    }

INSTALLED_APPS += ()

# Configuration for registration application

ACCOUNT_ACTIVATION_DAYS = 7

EMAIL_HOST = 'smtp-server.example.org'
EMAIL_HOST_USER = 'username'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_USE_TLS = True
EMAIL_PORT = 587


# vim:ft=python ts=4 tw=80 cc=+1:
