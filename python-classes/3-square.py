#!/usr/bin/python3
"""This module defines a Square class with an area method."""


class Square:
    """This class defines a square by its size."""

    def __init__(self, size=0):
        """Initialize a square with a validated private size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area."""
        return self.__size ** 2
