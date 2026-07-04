#!/usr/bin/python3
"""This module defines a custom object that can be pickled and unpickled."""

import pickle


class CustomObject:
    """Represent a custom object with name, age, and student status."""

    def __init__(self, name, age, is_student):
        """Initialize a CustomObject instance."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize the current object and save it to a pickle file."""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load and return a CustomObject instance from a pickle file."""
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception:
            return None
