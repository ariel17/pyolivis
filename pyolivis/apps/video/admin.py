#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Model registration for administration console.
"""
__author__ = "Ariel Gerardo Ríos (ariel.gerardo.rios@gmail.com)"
__version__ = "$Revision$"
__date__ = "$Date$"

from django.contrib import admin
from models import Video

admin.site.register(Video)

# vim:ft=python ts=4 tw=80 cc=+1:
