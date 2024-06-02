#!/usr/bin/python3
"""
Module that contains some classes
"""


class Fish:
    """Parent class representing a fish."""

    def swim(self):
        """Method to print that the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Method to print that the fish lives in water."""
        print("The fish lives in water")


class Bird:
    """Parent class representing a bird."""

    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class representing a flying fish, inheriting from both Fish and Bird."""

    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
