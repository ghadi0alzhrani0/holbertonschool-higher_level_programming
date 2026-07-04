#!/usr/bin/python3
"""This module defines a function that loads an object from a JSON file."""

import json


def load_from_json_file(filename):
    """Return the Python object stored inside a JSON file."""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
