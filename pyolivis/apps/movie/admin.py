#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Model registration for application Movie in administration console.
"""
__author__ = "Ariel Gerardo Ríos (ariel.gerardo.rios@gmail.com)"
__version__ = "$Revision$"
__date__ = "$Date$"

from django.contrib import admin
from models import Movie, Person, Role, Participation

admin.site.register(Movie)
admin.site.register(Person)
admin.site.register(Role)
admin.site.register(Participation)

# vim:ft=python ts=4 tw=80 cc=+1:
