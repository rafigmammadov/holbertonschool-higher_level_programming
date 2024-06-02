#!/usr/bin/python3
"""
Custom list class
"""


class VerboseList(list):
    """Custom list class that prints notifications when items
    are added or removed."""

    def append(self, item):
        """Append an item to the list and print a notification."""
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        """Extend the list with items from
        an iterable and print a notification."""
        super().extend(iterable)
        print(f"Extended the list with {len(iterable)} items.")

    def remove(self, item):
        """Remove an item from the list and print a notification."""
        if item in self:
            print(f"Removed {item} from the list.")
        else:
            print(f"{item} is not in the list.")
        super().remove(item)

    def pop(self, index=None):
        """Pop an item from the list and print a notification."""
        if index is None:
            popped_item = super().pop()
            print(f"Popped {popped_item} from the list.")
            return popped_item
        else:
            popped_item = super().pop(index)
            print(f"Popped {popped_item} from the list.")
            return popped_item
