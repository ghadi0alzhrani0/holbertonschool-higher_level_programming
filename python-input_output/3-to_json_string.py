#!/usr/bin/python3
"""This module defines a function that converts an object to JSON text."""

import json


def to_json_string(my_obj):
    """Return the JSON string representation of a Python object."""
    return json.dumps(my_obj)
