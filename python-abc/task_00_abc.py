#!/usr/bin/env python3
"""This module defines an abstract Animal class and its subclasses."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class that represents an animal."""

    @abstractmethod
    def sound(self):
        """Return the sound made by the animal."""
        pass


class Dog(Animal):
    """Class that represents a dog."""

    def sound(self):
        """Return the sound made by a dog."""
        return "Bark"


class Cat(Animal):
    """Class that represents a cat."""

    def sound(self):
        """Return the sound made by a cat."""
        return "Meow"
