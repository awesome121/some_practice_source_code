from random import *
from turtle import *


class Node:

    def __init__(self, item):
        self.data = item
        self.next_node = None


def add_item_to_list(first_node, item):
    """
    Adds item to end of linked list.
    first_node is the first node in the list.
    """
    if first_node is None:
        # the list needs a first node
        # initialise a first node with first_node = Node(item)
        # then call add_item_to_list to add another node
        #first_node = Node(item)
        #add_item_to_list(first_node, item)
        raise IndexError("None doesn't have a .next_node")
    else:
        new_node = Node(item)
        current_node = first_node
        # traverse list until at last node
        while current_node.next_node is not None:
            current_node = current_node.next_node
        # set last node's next pointer to point to the new node
        current_node.next_node = new_node


def slow_power(x, n):
    """Computes x to the power of n, the slow way!
    Named slow_power to distinguish it from quick_power, which you will write later.
    >>> slow_power(2, 2)
    4
    >>> slow_power(2, 3)
    8
    """
    if n == 0:
        return 1
    else:
        return x * slow_power(x, n - 1)


def gcd(a, b):
    """Computes the greatest common divisor of a and b."""
    if b == 0:
        return a
    elif a < b:
        return gcd(b, a)
    else:
        return gcd(a - b, b)


def str_length(s):
    """
    Calculates the length of a string.
    Definitely not the best way of doing this!
    Think about how much space all the sub lists will take up.
    """
    if s == "":
        return 0
    return 1 + str_length(s[1:])


def fib_recursive(n):
    """Returns the 'n'th Fibonacci number.
    >>> fib_recursive(0)
    0
    >>> fib_recursive(1)
    1
    >>> fib_recursive(2)
    1
    >>> fib_recursive(3)
    2
    >>> fib_recursive(4)
    3
    >>> fib_recursive(9)
    34
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n):
    """Returns the 'n'th Fibonacci number.
    >>> fib_iterative(0)
    0
    >>> fib_iterative(1)
    1
    >>> fib_iterative(2)
    1
    >>> fib_iterative(3)
    2
    >>> fib_iterative(4)
    3
    >>> fib_iterative(9)
    34
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_n_minus2 = 0
        fib_n_minus1 = 1      # start with fib of 2 which equals 1
        for i in range(1, n):  # there will be n+1 numbers including the 0'th
            curr_fib = fib_n_minus1 + fib_n_minus2
            fib_n_minus2 = fib_n_minus1
            fib_n_minus1 = curr_fib
        return curr_fib


def fibonacci_sequence(n):
    """
    Prints Fibonacci numbers up to the nth number (including the 0th number).

    >>> fibonacci_sequence(9)
    0 1 1 2 3 5 8 13 21 34
    """
    if n == 0:
        print(0, end='')
    else:
        fibonacci_sequence(n - 1)
        print(' ' + str(fib_recursive(n)), end='')


def tree(size, level):
    """
     Draws a funky fractal tree.
     Feel free to experiment with parameters...
     """
    if level != 0:
        forward(random() * size)
        x = pos()
        angle = random() * 20
        right(angle)
        tree(size * .8, level - 1)
        setpos(x)
        left(angle)
        angle = random() * -20
        right(angle)
        tree(size * .8, level - 1)
        left(angle)
        setpos(x)




#-------------------------------------------------------------------------
# Functions for students to implement
#-------------------------------------------------------------------------

def linked_list_length(list_node):
    """
    Returns the number of nodes in a linked list,
    0 if list is empty.

    >>> first_node = Node(1)
    >>> linked_list_length(first_node)
    1
    >>> add_item_to_list(first_node, 2)
    >>> linked_list_length(first_node)
    2
    >>> add_item_to_list(first_node, 3)
    >>> linked_list_length(first_node)
    3
    >>> add_item_to_list(first_node, 4)
    >>> linked_list_length(first_node)
    4
    >>> add_item_to_list(first_node, 10)
    >>> linked_list_length(first_node)
    5
    """
    # Note: you shouldn't be using a while loop here.
    # Think of the length of the list as the length of the first node (ie 1)
    # plus the length of the rest of the list.
    # Remember you should be using recursion so your function should
    # call linked_list_length at some stage!
    # ---start student section---
    if list_node == None:
        return 0
    elif list_node.next_node == None:
        return 1
    else:
        list_node = list_node.next_node
        return 1 + linked_list_length(list_node)
    # ===end student section===



def linked_list_print(list_node):
    """
    Prints list, one item per line.

    >>> first_node = Node(1)
    >>> linked_list_print(first_node)
    1
    >>> add_item_to_list(first_node, 2)
    >>> linked_list_print(first_node)
    1
    2
    >>> add_item_to_list(first_node, 3)
    >>> linked_list_print(first_node)
    1
    2
    3
    >>> add_item_to_list(first_node, 4)
    >>> linked_list_print(first_node)
    1
    2
    3
    4
    """
    # Note: you shouldn't be using a while loop here.
    # Remember you should be using recursion so your function should
    # call linked_list_print at some stage!
    # ---start student section---
    print(list_node.data)
    if list_node.next_node is not None:
        list_node = list_node.next_node
        linked_list_print(list_node)
    # ===end student section===



def linked_list_reverse_print(list_node):
    """
    Prints list in reverse, one item per line.

    >>> first_node = Node(1)
    >>> linked_list_reverse_print(first_node)
    1
    >>> add_item_to_list(first_node, 2)
    >>> linked_list_reverse_print(first_node)
    2
    1
    >>> add_item_to_list(first_node, 3)
    >>> linked_list_reverse_print(first_node)
    3
    2
    1
    >>> add_item_to_list(first_node, 4)
    >>> linked_list_reverse_print(first_node)
    4
    3
    2
    1
    """
    # Note: you shouldn't be using a while loop here.
    # Remember you should be using recursion so your function should
    # call linked_list_reverse_print at some stage!
    # Hint: make sure you aren't calling linked_list_print!
    # ---start student section---
    if list_node is None:
        return None
    else:
        
        linked_list_reverse_print(list_node.next_node)
        print(list_node.data)
        
        
        
    
    # ===end student section===



def is_in_linked_list(list_node, item):
    """
    Returns TRUE if item is in list, otherwise False.

    >>> first_node = Node(1)
    >>> is_in_linked_list(first_node,2)
    False
    >>> add_item_to_list(first_node, 2)
    >>> is_in_linked_list(first_node,2)
    True
    >>> add_item_to_list(first_node, 3)
    >>> add_item_to_list(first_node, 4)
    >>> add_item_to_list(first_node, 5)
    >>> is_in_linked_list(first_node,3)
    True
    >>> is_in_linked_list(first_node,10)
    False
    """
    # Note: you shouldn't be using a while loop here.
    # An item is in the list if it is in the list_node or in the rest of the list
    # The base case is when list_node is None (what should you return in this case?).
    # Remember you should be using recursion so your function should
    # call is_in_linked_list at some stage!
    # ---start student section---
    if list_node == None:
        return False
    elif list_node.data == item:
        return True
    return is_in_linked_list(list_node.next_node, item)
    # ===end student section===



def factorial(n):
    """
    Returns n!

    n must be >= 0
    Feel free to raise an exception if n is not valid.

    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(5)
    120
    """
    # ---start student section---
    if n < 0:
        raise ValueError('n must be larger than or equal to 0')
    elif n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)
    # ===end student section===



def quick_power(x, n):
    """
    Computes x ^ n where n is an integer and is >= 0
    Feel free to raise an exception if n is not valid.
    NOTES:
    - You need to write the doc test for the base case.
    - You shouldn't use the ** operator in your function
    - You shouldn't use the low_power function either
    - Remember n squared is simply n * n
    >>> quick_power(2,3)
    8
    >>> quick_power(2,8)
    256
    >>> quick_power(2,16)
    65536
    >>> quick_power(2,10)
    1024
    >>> quick_power(3, 2)
    9
    >>> quick_power(2, 9)
    512
    """
    # ---start student section---
    if n == 0:
        return 1
    elif n % 2 == 0:
        x_to_n_over2 = quick_power(x, n/2)
        return  x_to_n_over2 * x_to_n_over2 
    else:
        return x * quick_power(x, n-1)
    # ===end student section===



def recursive_string_print(s):
    """
    Prints a string out, one character per line, using recursion
    Think about why this is very inefficient for long strings!
    """
    # ---start student section---
    print(s[0])
    if len(s) > 1:
        recursive_string_print(s[1:])
    # ===end student section===



def recursive_reverse_string_print(s):
    """
    Prints a string out in reverse, one character per line, using recursion
    Feel free to use list slicing - but do think about why this is very
    inefficient for long strings!
    """
    # ---start student section---
    if len(s) == 1:
        print(s[-1])
    else:
        recursive_reverse_string_print(s[1:])
        print(s[0])
        
    # ===end student section===




def rec_print_list(alist, start_index=0):
    """ Takes a PYTHON list and prints out all the elements in the list (by default).
    If an index is provided, prints out all the items starting from that index.
    The items are printed one per line, from the first to the last item.
    NOTE:
    Your funciton should do this without list slicing as this will be more efficient.
    By list slicing we mean expressions such as alist[1:]
    """
    # ---start student section---
    if start_index == len(alist) - 1:
        print(alist[-1])
    else:
        print(alist[start_index])
        rec_print_list(alist, start_index+1)
    # ===end student section===

def rec_linked_list_append(first_node, item):
    """Using recursion to implement append for a linked list
    >>> first_node = Node(1)
    >>> rec_linked_list_append(first_node, 1)
    >>> rec_linked_list_append(first_node, 2)
    >>> rec_linked_list_append(first_node, 3)
    >>> linked_list_print(first_node)
    1
    1
    2
    3
    """
    if first_node.next_node == None:
        first_node.next_node = Node(item)
    else:
        rec_linked_list_append(first_node.next_node, item)
    
    




if __name__ == '__main__':
    # These imports are here to save you stress when submitting functions
    # to the quiz server. Normally they would go at the start of the module.
    import doctest
    import os
    os.environ['TERM'] = 'linux'  # Suppress ^[[?1034h


    # Uncomment next line to run the tests
    doctest.testmod()

    # Uncomment individual doctest runs below
    doctest.run_docstring_examples(linked_list_length, None)
    doctest.run_docstring_examples(linked_list_print, None)
    doctest.run_docstring_examples(linked_list_reverse_print, None)
    doctest.run_docstring_examples(is_in_linked_list, None)
    doctest.run_docstring_examples(factorial, None)
    doctest.run_docstring_examples(quick_power, None)
    doctest.run_docstring_examples(rec_linked_list_append, None)
    

    #Some other interesting tests to run:
    #-----------------------------------
    #n = 5000
    #print('fib({0:d}) = {1:d}'.format(n,fib_iterative(n)))
    #print('\n')

    #n = 100
    #print('fib({0:d}) = {1:d}'.format(n,fib_iterative(n)))
    #print('\n')

    #n = 31
    #print('fib({0:d}) = {1:d}'.format(n,fib_recursive(n)))
    #print('\n')

    #Given the value for fib_iterative(100) would it be wise
    #to try to run fib_recursive(100)????
