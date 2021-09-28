"""Module containing a basic priority queue."""
from stats import StatCounter, KEY_COMPS


class BasicPriorityQueue():
    """Basic implementation of a binary max-heap based priority queue."""

    def __init__(self, initial_items=None):
        """Makes a new priority queue containing initial_items."""
        self._comparisons = 0
        self._items = []
        if initial_items is not None:
            self._items = initial_items
            self._heapify()

    def __len__(self):
        """The length of a priority queue is the number of items it contains."""
        return len(self._items)

    def __repr__(self):
        """The priority queue representation is just its items."""
        return repr(self._items)

    def _heapify(self):
        """Converts the list to heap order. This is equivalent to inserting
        each item one at a time into the heap. There is a more efficient
        way
        """
        for index in range(1, len(self)):
            self._sift_up(index)

    def _parent_index(self, index):
        """Returns the index of the parent of the given index or -1 if the
        index has no parent (i.e., is root or not even in the list). Note the
        list items is 0-indexed, i.e., the root _item is at position 0.
        """
        parent = (index - 1) // 2
        if 0 < index < len(self):
            return parent
        return -1

    def _children_indices(self, index):
        """Returns the indices of the children of the given index. Any
        child index larger than or equal to the number of items is omitted.
        This results in an empty list being returned in the case where the
        item is terminal (has no children) in the binary heap. The empty list
        should also be returned if index is out of bounds of _items. Note the
        list _items is 0-indexed, i.e. the root item is at position 0.
        """
        left, right = index * 2 + 1, index * 2 + 2
        if left >= len(self):
            return []
        elif right >= len(self):
            return [left]
        else:
            return [left, right]

    def _max_child_index(self, index):
        """Returns the index of the first child with the maximal item value of any
        children of the node at the given index.
        If the node at the given index has no children then returns -1.
        """
        child_indices = self._children_indices(index)
        if len(child_indices) == 0:
            return -1
        max_child_index = child_indices[0]
        for i in child_indices[1:]:
            self._comparisons += 1
            item = self._items[i]
            max_item = self._items[max_child_index]
            if item > max_item:
                max_child_index = i
        return max_child_index

    def _swap_items(self, index, swap_index):
        """Swaps the items at the given indices in the heap."""
        self._items[index], self._items[swap_index] = self._items[swap_index], self._items[index]

    def _sift_up(self, index):
        """Moves the item at the given index up through the heap until it finds
        the correct place for it. That is, the item is moved up through the heap
        while it is larger than its parent.
        Notice the beauty of recursion.
        To carry out the sift up, the function simply swaps with the parent
        if needed and then sifts up from the parent...
        """
        parent_index = self._parent_index(index)
        # remember max_child is -1 if there aren't any children
        if parent_index >= 0:
            self._comparisons += 1
            if self._items[index] > self._items[parent_index]:
                self._swap_items(index, parent_index)
                self._sift_up(parent_index)

    def _sift_down(self, index):
        """Moves an item at the given index down through the heap until it finds
        the correct place for it. That is, the item is moved down through the
        heap while it is smaller than at least one of its children.
        Notice the beauty of recursion :)
        """
        max_child_index = self._max_child_index(index)
        # remember max_child is -1 if there aren't any children
        if max_child_index > 0:
            self._comparisons += 1
            if self._items[index] < self._items[max_child_index]:
                self._swap_items(index, max_child_index)
                self._sift_down(max_child_index)

    def insert(self, item):
        """Inserts a given item into the heap."""
        self._items.append(item)
        self._sift_up(len(self) - 1)

    def peek_max(self):
        """Returns the largest item in the heap."""
        return self._items[0]

    def pop_max(self):
        """Removes the largest item in the heap and returns it. Returns None if
        there are no items in the heap. Can be thought of as popping the max
        item off the heap.
        """
        if len(self) == 0:
            return None
        max_item = self.peek_max()
        self._items[0] = self._items[-1]
        self._items.pop(-1)
        self._sift_down(0)
        return max_item

    def get_comparisons(self):
        """Returns the total number of item comparisons the heap has made."""
        return self._comparisons

    def reset_comparisons(self):
        """Sets the number of item comparisons to zero."""
        self._comparisons = 0

    def validate(self):
        """Validates the heap.
        Returns True if the heap is a valid max-heap, and
        False otherwise.
        Note: The internal key comparison counter is turned off for this method.
        This is because it is used in testing and we don't want the comparisons
        to be counted toward the operations we are testing...
        """
        StatCounter.lock_counter(KEY_COMPS)
        result = True
        for index in range(1, len(self)):
            parent = self._parent_index(index)
            if self._items[parent] < self._items[index]:
                result = False
                break
        StatCounter.unlock_counter(KEY_COMPS)
        return result
