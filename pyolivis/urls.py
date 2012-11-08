#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: URL dispatcher configuration.
"""
__author__ = "Ariel Gerardo Ríos (ariel.gerardo.rios@gmail.com)"


from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pyolivis.views.home', name='home'),
    # url(r'^pyolivis/', include('pyolivis.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Search engine application
    url(r'^search/', include('pyolivis.apps.search.urls')),
)

# vim:ft=python ts=4 tw=80 cc=+1:
