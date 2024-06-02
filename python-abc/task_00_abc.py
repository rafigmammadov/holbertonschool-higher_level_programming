#!/usr/bin/python3
"""A module defining an abstract base
class Animal and its subclasses Dog and Cat."""


from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""
    @abstractmethod
    def sound(self):
        """Abstract method for producing animal sounds."""
        pass


class Dog(Animal):
    """Subclass representing a dog."""
    def sound(self):
        """Return the sound of a dog."""
        return "Bark"


class Cat(Animal):
    """Subclass representing a cat."""
    def sound(self):
        """Return the sound of a cat."""
        return "Meow"
