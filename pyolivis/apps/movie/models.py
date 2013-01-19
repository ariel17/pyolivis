#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Model classes definitions for Movie application.
"""
__author__ = "Ariel Gerardo Ríos (ariel.gerardo.rios@gmail.com)"


from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Movie(models.Model):
    """
    Stores all information about a movie in site.
    """

    RATING_MIN_VALUE = 0
    RATING_MAX_VALUE = 100

    user = models.ForeignKey(User, help_text=u"The user who has or will "
            " upload the movie.")
    name = models.CharField(max_length=100, help_text=u"The movie's name, as "
            "it was created.")
    slug = models.SlugField(help_text=u"An slug field for URL access.")
    synopsis = models.TextField(blank=True, help_text=u"A general view about "
            "the movie content.")
    rating = models.FloatField(validators=[MinValueValidator(RATING_MIN_VALUE),
        MaxValueValidator(RATING_MAX_VALUE)], default=RATING_MIN_VALUE,
        help_text=u"A decimal number representing a subjetive evaluation about"
            " the quality of the movie itself (Use references as %d='bad'; %d="
            "'very good'." % (RATING_MIN_VALUE, RATING_MAX_VALUE))

    def __unicode__(self):
        return u"<Movie id=%d user_id=%d name='%s' slug='%s' rating=%d>" % (
                self.id, self.user.id, self.name, self.slug, self.rating)


class Person(models.Model):
    """
    TODO: add some docstring for Person
    """

    first_name = models.CharField(max_length=100, help_text="TODO")
    last_name = models.CharField(max_length=100, help_text="TODO")
    # TODO profile?

    def __unicode__(self):
        return u"<Person id=%d first_name='%s' last_name='%s'>" % (self.id,
                self.first_name, self.last_name)


class Role(models.Model):
    """
    TODO: add some docstring for Role
    """

    name = models.CharField(max_length=50, help_text="TODO")
    description = models.TextField(blank=True, help_text="TODO")

    def __unicode__(self):
        return u"<Role id=%d name='%s'>" % (self.id, self.name)


class Participation(models.Model):
    """
    TODO: add some docstring for Participation
    """

    role = models.ForeignKey(Role, help_text="TODO")
    movie = models.ForeignKey(Movie, help_text="TODO")
    person = models.ForeignKey(Person, help_text="TODO")

    def __unicode__(self):
        return u"<Participation id=%d role=%s movie=%s person=%s>" % (self.id,
                self.role, self.movie, self.person)
