#!/usr/bin/env python3
"""This module defines a counted iterator class."""


class CountedIterator:
    """An iterator that counts the number of fetched items."""

    def __init__(self, iterable):
        """Initialize the iterator and the counter."""
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Return the next item and update the counter."""
        item = next(self.iterator)
        self.count += 1
        return item

    def __iter__(self):
        """Return the iterator object itself."""
        return self

    def get_count(self):
        """Return the number of items already fetched."""
        return self.count
