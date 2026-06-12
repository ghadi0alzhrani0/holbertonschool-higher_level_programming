#!/usr/bin/python3
"""This module prints a square.

It contains a function that prints a square using the # character.
The size must be an integer.
"""


def print_square(size):
    """Print a square with the character #.

    Args:
        size: The length of the square.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
