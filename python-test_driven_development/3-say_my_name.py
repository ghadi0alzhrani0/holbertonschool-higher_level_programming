#!/usr/bin/python3
"""This module prints a full name.

It contains a function that prints a first name and a last name.
Both names must be strings.
The last name is optional.
"""


def say_my_name(first_name, last_name=""):
    """Print a name in the format: My name is first_name last_name.

    Raises TypeError if first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
