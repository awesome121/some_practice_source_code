"""Module containing some methods for finding the largest k
items in a list.
"""
from basic_priority_queue import BasicPriorityQueue
from dheap_priority_queue import DheapPriorityQueue
# import the following when you are ready to use it
# rom dheap_priority_queue import DheapPriorityQueue



def top_k_select(items, k):
    """Uses a modified max-selection sort to find the max k items of a list.
    This sort terminates once the max k values are found. Note that
    this function does not modify the list items. This function returns
    a descending list of the top k items and the number of item comparisons
    made, ie, it returns result_list, comparisons.
    Hint: have the fillslot at the start and fill it with the max each time...
    """
    items = list(items)  # Makes a copy of items.
    comparisons = 0
    # ---start student section---
    fillslot = 0
    while fillslot != k: 
        max_index = fillslot
        for i in range(fillslot, len(items)):
            comparisons += 1
            if items[i] > items[max_index]:
                max_index = i
        items[fillslot], items[max_index] = items[max_index], items[fillslot]
        fillslot += 1   
    return items[:fillslot], comparisons
    # ===end student section===


def top_k_heap(items, k):
    """Uses a BasicPriorityQueue to find the max k items of a list. Note this
    function does not modify the list items. This function returns
    a descending list of the top k items and the number of item comparisons
    made, ie, it returns result_list, comparisons
    """
    items = list(items)  # Makes a copy of items.
    top = []
    p_queue = BasicPriorityQueue(items)
    # ---start student section---
    i = 1
    while i <= k:
        top.append(p_queue.pop_max())
        i += 1
    return top, p_queue.get_comparisons() 
    # ===end student section===


def top_k_dheap(items, k, branch_factor):
    """Uses a DheapPriorityQueue to find the max k items of a list. Note this
    function does not modify the list items. This function returns
    a descending list of the top k items and the number of item comparisons
    made, ie, it returns (result_list, comparisons)
    Complete this function once you have your dheap working.
    """
    # ---start student section---
    result_list = []
    items = list(items)
    dh_queue = DheapPriorityQueue(items, branch_factor)
    i = 1
    while i <= k:
        result_list.append(dh_queue.pop_max())
        i += 1
    return result_list, p_queue.get_comparisons() 
    # ===end student section===


