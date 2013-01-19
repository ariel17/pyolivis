#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Model classes definitions for Movie application.
"""
__author__ = "Ariel Gerardo Ríos (ariel.gerardo.rios@gmail.com)"


from django.db import models


class Movie(models.Model):
    """
    Stores all information about a movie in site.
    """

    RATING_MIN_VALUE = 0
    RATING_MAX_VALUE = 100

    user = models.ForeignKey(User, help_text=u"The user who has or will upload"\
            " the movie.")
    name = models.CharField(max_length=100, help_text=u"The movie's name, as "\
            "it was created.")
    slug = models.SlugField(help_text=u"An slug field for URL access.")
    synopsis = models.TextField(blank=True, help_text=u"A general view about "\
            "the movie content.")
    rating = models.Float(min_value=RATING_MIN_VALUE, max_value=\
            RATING_MAX_VALUE, default=RATING_MIN_VALUE, help_text=u"A decimal "\
            "number representing a subjetive evaluation about the quality of "\
            "the movie itself (Use references as %d='bad'; %d='very good'." %
                (RATING_MIN_VALUE, RATING_MAX_VALUE))

    def __unicode__(self):
        return u"<Movie id=%d user_id=%d name='%s' slug='%s' rating=%d>" % (id,
                user.id, name, slug, rating)
