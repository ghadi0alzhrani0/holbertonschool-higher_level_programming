#!/usr/bin/python3
"""This module defines a function that appends text to a UTF-8 file."""


def append_write(filename="", text=""):
    """Append text to a UTF-8 file and return the number of characters."""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
