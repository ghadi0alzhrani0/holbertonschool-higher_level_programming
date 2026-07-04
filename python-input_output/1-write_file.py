#!/usr/bin/python3
"""This module defines a function that writes text to a UTF-8 file."""


def write_file(filename="", text=""):
    """Write text to a UTF-8 file and return the number of characters."""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
