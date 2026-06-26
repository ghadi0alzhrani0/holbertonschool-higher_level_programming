#!/usr/bin/env python3
"""This module defines classes to demonstrate multiple inheritance."""


class Fish:
    """Class that represents a fish."""

    def swim(self):
        """Print a fish swimming message."""
        print("The fish is swimming")

    def habitat(self):
        """Print a fish habitat message."""
        print("The fish lives in water")


class Bird:
    """Class that represents a bird."""

    def fly(self):
        """Print a bird flying message."""
        print("The bird is flying")

    def habitat(self):
        """Print a bird habitat message."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class that represents a flying fish."""

    def fly(self):
        """Print a flying fish flying message."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print a flying fish swimming message."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print a flying fish habitat message."""
        print("The flying fish lives both in water and the sky!")
