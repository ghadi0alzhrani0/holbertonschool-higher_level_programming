#!/usr/bin/env python3
"""This module defines mixins and a Dragon class."""


class SwimMixin:
    """Mixin that gives swimming behavior."""

    def swim(self):
        """Print a swimming message."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that gives flying behavior."""

    def fly(self):
        """Print a flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Class that represents a dragon with mixed abilities."""

    def roar(self):
        """Print a dragon roaring message."""
        print("The dragon roars!")
