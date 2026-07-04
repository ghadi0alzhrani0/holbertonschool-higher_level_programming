#!/usr/bin/python3
"""This module defines a function that reads a UTF-8 text file."""


def read_file(filename=""):
    """Read a UTF-8 text file and print its content to standard output."""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
