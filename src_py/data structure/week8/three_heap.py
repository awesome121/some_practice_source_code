""" A module dedicated to the three heap """
import doctest
import os


#--------------------------------------------------------------------------
def load_file(file_name):
    """ Returns a list of numbers from the file.
        The file should contain one integer per line.
    """
    with open(file_name) as infile:
        lines = infile.read().splitlines()
    nums = [int(line) for line in lines]
    return nums

#-------------------------------------------------
#-------------------------------------------------
class Heap(object):
    """An abstract interface for a Heap."""
    def __init__(self):
        # Create a list to store heap items.
        self._items = [0]

    def insert(self, item):
        #don't implement here
        #this is just a place holder
        pass

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        """Returns the actual length of the heap,
        ie, how many items are in the heap"""
        return len(self._items) - 1

    def __repr__(self):
        """Returns only the items in the heap,
        ie, leaves out _items[0] as the heap
        data starts from index 1..."""
        return repr(self._items[1:])


#-------------------------------------------------
#-------------------------------------------------
class Max_3_Heap(Heap):
    """Implementation of a max-three-heap.
    Each child must be smaller than or equal to its parent.
    Each parent has up to 3 children.
    First element of the heap is stored in _items[1]
    left_child_index = parent_index*3-1
    middle_child_index = parent_index*3
    right_child_index = parent_index*3+1

    parent = (child+1)//3"""

    def __init__(self):
        super(Max_3_Heap, self).__init__()

    #-------------------------------------------------
    def insert(self, item):
        """Inserts a given item into the heap.

        >>> h = Max_3_Heap()
        >>> h.insert(3)
        >>> h._items
        [0, 3]
        >>> h.insert(7)
        >>> h._items
        [0, 7, 3]
        >>> h.insert(5)
        >>> h._items
        [0, 7, 3, 5]
        >>> h.insert(2)
        >>> h._items
        [0, 7, 3, 5, 2]
        >>> h.insert(6)
        >>> h._items
        [0, 7, 6, 5, 2, 3]
        """
        # Append the item to the end of the heap
        self._items.append(item)
        # Sift it up into place
        self._sift_up(len(self._items)-1)


    #-------------------------------------------------
    def _sift_up(self, index):
        """
        Moves the item at the given index up through the heap until it finds
        the correct place for it. That is, the item is moved up through the heap
        while it is larger than its parent.
        """
        # ---start student section---
        parent = (index+1) // 3
        # While we haven't reached the top of the heap, and its parent is
        # smaller than the item
        if index > 1 and self._items[index] > self._items[parent]:
            # Swap the item and its parent
            self._items[index], self._items[parent] = self._items[parent], self._items[index]
            # Carry on sifting up from the parent index
            self._sift_up(parent)
        # else no more sifting needed as didn't swap.
        # ===end student section===

    #-------------------------------------------------
    def peek_max(self):
        """
        Returns the largest value in the heap, ie, the
        top of the heap. Doesn't change the heap.

        >>> h = Max_3_Heap()
        >>> h.insert(5)
        >>> h.validate()
        True
        >>> h.peek_max()
        5
        >>> h.insert(3)
        >>> h.peek_max()
        5
        >>> h.insert(7)
        >>> h.peek_max()
        7
        """
        if len(self._items) > 1:
            return self._items[1]
        else:
            return None

    #-------------------------------------------------
    def pop_max(self):
        """
        Removes the largest item in the heap and returns it. Returns None if
        there are no items in the heap. Can be thought of as Popping the max
        item off the heap.

        >>> h = Max_3_Heap()
        >>> h.insert(5)
        >>> h.pop_max()
        5
        >>> len(h)
        0
        >>> h.insert(3)
        >>> h.insert(7)
        >>> h.pop_max()
        7
        >>> h.pop_max()
        3
        >>> len(h)
        0
        >>> tmp = [h.insert(item) for item in [3, 7, 5, 2, 4]]
        >>> print(h)
        [7, 4, 5, 2, 3]
        >>> h.pop_max()
        7
        >>> h._items[1]
        5
        >>> h._items[2]
        4
        >>> h.pop_max()
        5
        >>> print(h)
        [4, 2, 3]
        >>> h.pop_max()
        4
        >>> h.pop_max()
        3
        >>> h.pop_max()
        2
        >>> h = Max_3_Heap()
        >>> h.insert(1)
        >>> h.insert(5)
        >>> h.insert(2)
        >>> h.insert(7)
        >>> h.validate()
        True
        >>> h.pop_max()
        7
        >>> h.validate()
        True
        """
        if len(self._items)>1:
            max_item = self._items[1]
            if len(self._items) > 2:
                # If there are more items in the heap, swap the last one with the
                # first, and sift it down
                self._items[1] = self._items.pop()
                self._sift_down(1)
            else:
                # Otherwise, remove the item - it is the last one
                self._items.pop()
            return max_item
        else:
            return None

    #-------------------------------------------------
    def _sift_down(self, index):
        """
        Moves an item at the given index down through the heap until it finds
        the correct place for it. That is, the item is moved down through the
        heap while it is larger than any of its children.
        """
        # ---start student section---
        if (index * 3-1) <= len(self._items)-1:
            left, middle, right = 3 * index - 1, 3 * index, 3 * index + 1
            if self._items[index] < self._items[left]:
                self._items[left], self._items[index] = self._items[index], self._items[left]
                self._sift_down(left)
            elif middle <= len(self._items)-1:
                if self._items[index] < self._items[middle]:
                    self._items[middle], self._items[index] = self._items[index], self._items[middle]
                    self._sift_down(middle)                
                elif right <= len(self._items)-1:
                    if self._items[index] < self._items[right]:
                        self._items[right], self._items[index] = self._items[index], self._items[right]
                        self._sift_down(right)                  
        # ===end student section===


    #-------------------------------------------------
    def validate(self):
        """
        Validates the heap. Returns True if the heap is a valid max-3-heap, and
        False otherwise.

        >>> h = Max_3_Heap()
        >>> h._items = [0, 5, 3, 1]
        >>> h.validate()
        True
        >>> h._items = [0, 100, 90, 40, 30, 80, 60, 30, 11]
        >>> h.validate()
        True
        >>> h._items = [0, 7, 6, 1, 8]
        >>> h.validate()
        False
        """

        # ---start student section---
        index = 1
        left, middle, right = 3 * index - 1, 3 * index, 3 * index + 1
        while left <= len(self._items)-1:
            if self._items[index] < self._items[left]:
                return False
            if middle <= len(self._items)-1:
                if self._items[index] < self._items[middle]:
                    return False
            if right <= len(self._items)-1:
                if self._items[index] < self._items[right]:
                    return False
            index += 1
            left, middle, right = 3 * index - 1, 3 * index, 3 * index + 1
        return True
        # ===end student section===



if __name__ == '__main__':
    os.environ['TERM'] = 'linux' # Suppress ^[[?1034h
    doctest.testmod()

    my_heap = Max_3_Heap()
    for item in [20,18,13,15,11,12,16,10,9,11,13,2,9,10,1]:
        my_heap.insert(item)

    #think of two ways to print a view of the heap



