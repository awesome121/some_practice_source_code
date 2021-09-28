"""Data structures implemented with linked lists.

Check out the comments/code at the end of this module
for how to run the provided doctests.

You should start by implementing the __str__ method as most
tests will print out Stacks or Queues. Hint, while loops will
be handy here.

"""

import doctest
import os


class Node:
    """A node for a linked list."""

    def __init__(self, initdata):
        self.data = initdata
        self.next_node = None


class Stack(object):
    """ Implements a Stack using a Linked List
    >>> s = Stack()
    >>> print(s)
    List for stack is: None
    >>> result = s.pop()
    Traceback (most recent call last):
    ...
    IndexError: Can't pop from empty stack.
    >>> s.push('a')
    >>> print(s)
    List for stack is: a -> None
    >>> len(s)
    1
    >>> print(s.head.data)
    a
    >>> print(s.head.next_node)
    None
    >>> s.pop()
    'a'
    >>> print(s)
    List for stack is: None
    >>> s.push('b')
    >>> print(s)
    List for stack is: b -> None
    >>> s.push('c')
    >>> print(s)
    List for stack is: c -> b -> None
    >>> len(s)
    2
    >>> s.peek()
    'c'
    >>> print(s)
    List for stack is: c -> b -> None
    >>> s.pop()
    'c'
    >>> print(s)
    List for stack is: b -> None
    >>> e = Stack()
    >>> e.peek()
    Traceback (most recent call last):
    ...
    IndexError: Can't peek at empty stack.
    """

    def __init__(self):
        self.head = None

    def push(self, item):
        """push a new item on to the stack"""
        # ---start student section---
        next_node = self.head
        self.head = Node(item)
        self.head.next_node = next_node
        # ===end student section===

    def pop(self):
        """pop an item off the top of the stack, and return it
        If stack is empty you should raise an IndexError as per
        the comment below."""
        # use the following line to raise error when stack is empty
        # raise IndexError("Can't pop from empty stack.")
        # ---start student section---
        if self.head == None:
            raise IndexError("Can't pop from empty stack.")
        else:
            result = self.head.data
            self.head = self.head.next_node
            return result
        # ===end student section===

    def peek(self):
        """pop an item on the top of the top of the stack, but don't remove it.
        If stack is empty you should raise an IndexError as per
        the comment below.
        """
        # use the following line to raise error when stack is empty
        # raise IndexError("Can't peek at empty stack.")
        # ---start student section---
        if self.head == None:
            raise IndexError("Can't peek at empty stack.")
        else:
            return self.head.data
        # ===end student section===

    def is_empty(self):
        """ Returns True if stack is empty """
        return self.head is None

    def __len__(self):
        """ Returns the length --- calling len(s) will invoke this method """
        # ---start student section---
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.next_node
        return count
        # ===end student section===

    def __str__(self):
        """Returns a string representation of the list for the stack starting
        from the beginning of the list. Items are separated by ->
        and ending with -> None
        See doctests in class docstring
        """
        # ---start student section---
        result = 'List for stack is: '
        count = 0
        current = self.head
        while current != None:
            result += current.data + ' -> '
            current = current.next_node
        result = result + 'None'
        return result
        # ===end student section===


class Queue(object):
    """ Implements a Queue using a Linked List"
    >>> q = Queue()
    >>> len(q)
    0
    >>> print(q)
    List for queue is: None
    >>> result = q.dequeue()
    Traceback (most recent call last):
    ...
    IndexError: Can't dequeue from empty queue.
    >>> q.enqueue('a')
    >>> print(q)
    List for queue is: a -> None
    >>> len(q)
    1
    >>> q.enqueue('b')
    >>> print(q)
    List for queue is: a -> b -> None
    >>> q.enqueue('c')
    >>> print(q)
    List for queue is: a -> b -> c -> None
    >>> len(q)
    3
    >>> q.dequeue()
    'a'
    >>> print(q)
    List for queue is: b -> c -> None
    """

    def __init__(self):
        self.head = None

    def enqueue(self, item):
        """Add an item onto the tail of the queue.
        Note: The front of the queue is stored at the head of the list 
        so adding to the rear requires finding the end of the list
        """
        # ---start student section---
        current = self.head
        if current == None:
            self.head = Node(item)
            self.head.next_node = None
        else:
            while current.next_node != None:
                current = current.next_node
            current.next_node = Node(item)
            current.next_node.next_node = None
        # ===end student section===

    def dequeue(self):
        """Remove an item from the head of the queue and return it.
        If queue is empty you should raise an IndexError as per
        the comment below."""
        # use the following line to raise error when queue is empty
        # raise IndexError("Can't dequeue from empty queue.")
        # ---start student section---
        if self.head == None:
            raise IndexError("Can't dequeue from empty queue.")
        else:
            removed = self.head
            self.head = removed.next_node
            return removed.data
        # ===end student section===

    def is_empty(self):
        """ returns True if the queue is empty """
        # ---start student section---
        return self.head == None
        # ===end student section===

    def __len__(self):
        """ Returns the length --- calling len(q) will invoke this method """
        # ---start student section---
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next_node
        return count
        # ===end student section===

    def __str__(self):
        """Returns a string representation of the list for the queue starting
        from the beginning of the list. Items are separated by ->
        and ending with -> None
        See doctests in class docstring
        """
        # ---start student section---
        result = 'List for queue is: '
        count = 0
        current = self.head
        while current != None:
            result += current.data + ' -> '
            current = current.next_node
        result = result + 'None'
        return result
        # ===end student section===


if __name__ == '__main__':
    os.environ['TERM'] = 'linux'  # Suppress ^[[?1034h
    
    
    # Ucomment the relevant doc test run line below
    # Be careful your can get infinite loops if done wrong... so try with Debug
    doctest.run_docstring_examples(Stack, None)
    doctest.run_docstring_examples(Queue, None)
    
    
    # Uncomment the testmod() line to run all the tests
    # Can enter an infinite loop if your Stack isn't implemented correctly
    # doctest.testmod()
