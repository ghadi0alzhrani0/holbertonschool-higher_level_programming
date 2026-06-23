#!/usr/bin/python3
"""This module defines a function that lists object attributes and methods."""


def lookup(obj):
    """Return the list of available attributes and methods of an object."""
    return dir(obj)
