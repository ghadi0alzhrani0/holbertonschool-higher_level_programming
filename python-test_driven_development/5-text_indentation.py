#!/usr/bin/python3
"""This module prints text with indentation.

It contains a function that prints two new lines after
each '.', '?' and ':' character.
"""


def text_indentation(text):
    """Print text with two new lines after '.', '?' and ':'.

    Args:
        text: The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    line = ""

    for char in text:
        line += char

        if char in ".?:":
            print(line.strip())
            print()
            line = ""

    if line.strip() != "":
        print(line.strip(), end="")
