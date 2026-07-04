#!/usr/bin/python3
"""This module defines a Student class with filtered JSON output."""


class Student:
    """Represent a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student with public instance attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation, optionally filtered by attrs."""
        if isinstance(attrs, list):
            return {
                key: getattr(self, key)
                for key in attrs
                if isinstance(key, str) and hasattr(self, key)
            }
        return self.__dict__.copy()
