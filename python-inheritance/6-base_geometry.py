#!/usr/bin/python3
"""This module defines a base geometry class with an area method."""


class BaseGeometry:
    """This class represents a base geometry structure."""

    def area(self):
        """Raise an exception because area is not implemented."""
        raise Exception("area() is not implemented")
