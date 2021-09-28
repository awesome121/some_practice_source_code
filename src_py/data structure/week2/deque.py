import doctest
import os


class Deque(object):
    """
    Implements a Deque using a Python list internally.
    >>> d = Deque()
    >>> d.enqueue_front('a')
    >>> d.dequeue_front()
    'a'
    >>> d.enqueue_front('a')
    >>> d.enqueue_rear('b')
    >>> len(d)
    2
    >>> d.dequeue_rear()
    'b'
    >>> len(d)
    1
    """
    def __init__(self):
        self._data = []

    def enqueue_front(self, item):
        """Add an item onto the front of the deque."""
        self._data.insert(0, item)

    def enqueue_rear(self, item):
        """Add an item onto the rear of the deque."""
        self._data.append(item)

    def dequeue_front(self):
        """Remove an item from the front of the deque and return it."""
        if self.is_empty():
            raise IndexError("Can't dequeue_front from an empty deque!")
        else:
            # Not empty so remove front item and return it
            # ---start student section---
            return self._data.pop(0)
            # ===end student section===

    def dequeue_rear(self):
        """Remove an item from the rear of the deque and return it."""
        if self.is_empty():
            raise IndexError("Can't dequeue_rear from an empty deque!")
        else:
            # Not empty so remove rear item and return it
            # ---start student section---
            return self._data.pop()
            # ===end student section===

    def is_empty(self):
        """ Returns True if the deque is empty."""
        return len(self._data) == 0

    def __len__(self):
        """ Returns the number of items in the deque."""
        return len(self._data)

    def __repr__(self):
        """ Returns a string representing the deque."""
        return "Front-> " + repr(self._data) + " <-Rear"



# These are the similar to the doctests provided
