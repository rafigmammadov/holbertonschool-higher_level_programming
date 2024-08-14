#!/usr/bin/python3
"""
Script that contains LockedClass class
"""

class LockedClass:
    """
    a class LockedClass with no class or object attribute
    """
    def __setattr__(self, key, value):
        if key not in ('first_name', ):
            raise AttributeError(f"'LockedClass' object has no attribute '{name}'")
        super().__setattr__(key, value)
