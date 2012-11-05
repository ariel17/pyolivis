#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Development project settings.
"""
__author__ = "Ariel Gerardo Ríos (ariel.gerardo.rios@gmail.com)"


from common import *


DEBUG = True

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

# vim:ft=python ts=4 tw=80 cc=+1:
