#!/usr/bin/python3
"""This module defines an integer addition function.

It contains a function that adds two numbers.
The function accepts integers and floats only.
Floats are converted to integers before addition.
"""


def add_integer(a, b=98):
    """Return the addition of two integers.

    Floats are converted to integers first.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
