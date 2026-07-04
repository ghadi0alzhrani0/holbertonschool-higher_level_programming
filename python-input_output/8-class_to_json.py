#!/usr/bin/python3
"""This module defines a function that describes an object's attributes."""


def class_to_json(obj):
    """Return a dictionary of an object's attributes."""
    return obj.__dict__
