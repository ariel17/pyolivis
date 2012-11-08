#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Search application views definitions.
"""
__author__ = "Ariel Gerardo Ríos (ariel.gerardo.rios@gmail.com)"


from django.shortcuts import render_to_response


def index(request):
    """
    Shows the main screen when accessing the search engine.
    """
    return render_to_response('index.html')

# vim:ft=python ts=4 tw=80 cc=+1:
