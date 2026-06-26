#!/usr/bin/env python3
"""This module defines a verbose list class."""


class VerboseList(list):
    """A list that prints messages when modified."""

    def append(self, item):
        """Append an item to the list and print a message."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        """Extend the list with items and print a message."""
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Remove an item from the list and print a message."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item from the list and print a message."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
