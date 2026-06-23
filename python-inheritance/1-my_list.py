#!/usr/bin/python3
"""This module defines a custom list class."""


class MyList(list):
    """This class extends list with a sorted print method."""

    def print_sorted(self):
        """Print the list in ascending order."""
        print(sorted(self))
