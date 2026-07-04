#!/usr/bin/python3
"""This module defines a basic Student class."""


class Student:
    """Represent a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student with public instance attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dictionary representation of the student."""
        return self.__dict__
