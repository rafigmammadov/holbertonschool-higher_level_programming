#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, key, value):
        if key != 'first_name':
            raise AttributeError(f"'LockedClass' object has no attribute '{name}'")
        super().__setattr__(key, value)
