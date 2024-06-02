#!/usr/bin/python3
"""
Module that contains CountedIterator class
"""


class CountedIterator:
    """Custom iterator class that keeps track
    of the number of items iterated."""

    def __init__(self, iterable):
        """Initialize the iterator and counter."""
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Override the __next__ method to increment the counter."""
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration("No more items to iterate")

    def get_count(self):
        """Return the current value of the counter."""
        return self.count
