"""Module containing a priority queue that can remove arbitrary items."""
from basic_priority_queue import BasicPriorityQueue


class ChangePriorityQueue(BasicPriorityQueue):
    """Implementation of a binary max-heap based priority queue with remove
    item functionality.
    """

    def __init__(self, initial_items=None, initial_priorities=None):
        """Makes a new priority queue containing initial_items and uses
        the corresponding position in initial_priorities as the priority
        for each item.
        If initial_priorities is not provided then the priority for each
        item is simply set to the items index in the initial_items list.
        """
        if initial_items is not None and initial_priorities is not None:
            initial_indices = range(len(initial_items))
            self._item_indices = dict(zip(initial_items, initial_indices))
            items = list(zip(initial_priorities, initial_items))
            super().__init__(items)
        else:
            self._item_indices = dict()
            super().__init__()

    def insert(self, item):
        """Insert cannot be used in change_priority_queue as the priority must
        be explicitly given.
        """
        raise TypeError(
            "Also need priority. Call insert_with_priority instead!")

    def _swap_items(self, index, swap_index):
        """Swaps the items at the given indices in the heap and updates
        the _item_indices dictionary to be consistent with the change.
        """
        # ---start student section---
        key1, key2 = self._items[index][1], self._items[swap_index][1]     
        self._item_indices[key1], self._item_indices[key2] = swap_index, index
        super()._swap_items(index, swap_index)
        # ===end student section===


    def _max_child_index(self, index):
        """Returns the index of the first child with the maximal priority value
        of any  child of the node at the given index.
        If no such maximal child exists -1 is returned, ie, if there are no children.
        Note: this method is very similar to the basic priority queue but it
        needs to now look at the priotity value in the tuple that is store in each node.
        """
        # ---start student section---
        child_indices = super()._children_indices(index)
        if child_indices == []:
            return -1
        max_child_index = child_indices[0]
        if len(child_indices) == 2:
            item = self._items[child_indices[1]][0]
            max_item = self._items[max_child_index][0]
            self._comparisons += 1
            if item > max_item:
                max_child_index = child_indices[1]
        return max_child_index
        # ===end student section===


    def _sift_up(self, index):
        """Moves the item at the given index up through the heap until it finds
        the correct place for it. That is, the item is moved up through the heap
        while its priority is larger than its parent's priority.
        Notice the beauty of recursion.
        To carry out the sift up, the function simply swaps with the parent
        if needed and then sifts up from the parent...
        NOTE: This is very similar to the method in the basic class
        but this method should use the priorty to compare.
        Remember each node now stores (priority, item) tuples.
        """
        # ---start student section---
        parent_index = super()._parent_index(index)
        if parent_index >= 0:
            self._comparisons += 1
            if self._items[parent_index][0] < self._items[index][0]:
                self._swap_items(parent_index, index)
                self._sift_up(parent_index)
                
        # ===end student section===

    def _sift_down(self, index):
        """Moves an item at the given index down through the heap until it finds
        the correct place for it. That is, the item is moved down through the
        heap while its priority is smaller than at least one of its children's priorities.
        Notice the beauty of recursion :)
        NOTE: This is very similar to the method in the basic class
        but this method should use the priorty to compare.
        Remember each node now stores (priority, item) tuples.
        """
        # ---start student section---
        max_child_index = self._max_child_index(index)
        if max_child_index > 0:
            self._comparisons += 1
            if self._items[index][0] < self._items[max_child_index][0]:
                self._swap_items(index, max_child_index)
                self._sift_down(max_child_index)
        # ===end student section===

    def insert_with_priority(self, item, priority):
        """Inserts a given item into the heap with the given priority. Updates
        the _item_indices dictionary to be consistent with the insert.
        """
        # ---start student section---
        self._items.append((priority, item))
        self._item_indices[item] = len(self._items)-1
        self._sift_up(len(self)-1)
        # ===end student section===

    def peek_max(self):
        """Returns the largest item in the heap."""
        # ---start student section---
        return self._items[0][1]
        # ===end student section===

    def pop_max(self):
        """Removes the largest item in the heap and returns it.
        Note: just the item is returned, NOT the (key,item) tuple.
        Returns None if there are no items in the heap.
        Can be thought of as popping the max item off the heap.
        Updates the _item_indices dictionary to be consistent with the removal."""
        # ---start student section---
        if self._items == []:
            return None
        else:
            if len(self) == 1:
                item = self._items.pop()[1]
                self._item_indices.pop(item)
            else:
                item = self.peek_max()
                self._item_indices.pop(item)
                self._items[0] = self._items[-1]
                successor = self._items.pop()[1]
                self._item_indices[successor] = 0
                self._sift_down(0)
            return item
        # ===end student section===


    def remove_item(self, item):
        """Removes and returns a specific item from the priority queue.
        If the item is not in the priority queue this method does nothing
        and returns None. in the case of removal this method Updates the
        _item_indices dictionary to be consistent with the removal.
        """
        # ---start student section---
        if item in self._item_indices:
            index = self._item_indices[item]
            if len(self) != 1:
                priority, successor = self._items[-1]
                self._items[index] = priority, successor
                self._items.pop()
                self._item_indices.pop(item)
                self._item_indices[successor] = index
                self._sift_down(index)
            else:
                self._items.pop()
                self._item_indices.pop(item)
            return item
        return None
        # ===end student section===


