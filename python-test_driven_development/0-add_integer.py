#!/usr/bin/python3
"""This module contains an integer addition function.

The module provides a function that adds two numbers.
It checks the arguments before doing the addition.
Floats are converted to integers before adding.
"""


def add_integer(a, b=98):
    """Return the addition of two integers.

    Float values are converted to integers before the addition.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
