#!/usr/bin/python3
"""
Module that contains mixin classes
"""


class SwimMixin:
    """A mixin class with a swim method."""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """A mixin class with a fly method."""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A class representing a dragon with swimming and flying abilities."""

    def roar(self):
        print("The dragon roars!")
