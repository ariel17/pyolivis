#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: URL dispatcher configuration for 'search' application.
"""
__author__ = "Ariel Gerardo Ríos (ariel.gerardo.rios@gmail.com)"


from django.conf.urls import patterns, url

from views import *


urlpatterns = patterns('pyolivis.apps.search',
    url(r'^$', 'views.index', name='index'),
)

# vim:ft=python ts=4 tw=80 cc=+1:
