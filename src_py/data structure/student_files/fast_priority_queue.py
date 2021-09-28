"""Module containing a priority queue implemented as a binary heap with a
fast heapify method.
"""
from basic_priority_queue import BasicPriorityQueue


class FastPriorityQueue(BasicPriorityQueue):
    """Implementation of a binary max-heap based priority queue fast heapify."""

    def _heapify(self):
        """Converts the list to heap order. On average it uses
        considerably fewer comparisons than inserting each item
        individually.
        """
        index_last_parent = len(self._items)//2
        for p in range(index_last_parent, -1, -1):
            self._sift_down(p)
       
            