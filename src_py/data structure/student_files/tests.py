"""Module containing the unit tests for all questions."""
import unittest
import random
import string
from classes import *
from top_k import *
from stats import StatCounter, KEY_COMPS
from basic_priority_queue import BasicPriorityQueue
from change_priority_queue import ChangePriorityQueue
from dheap_priority_queue import DheapPriorityQueue
from fast_priority_queue import FastPriorityQueue


real_comparisons = StatCounter.get_count
lock_counter = StatCounter.lock_counter
unlock_counter = StatCounter.unlock_counter



class BaseTester(unittest.TestCase):
    """ Very simple base class that defines the setUp method """

    def setUp(self):
        """ Resets the internal counter """
        StatCounter.reset_counts()


class TestTopK(BaseTester):
    """Tests for Task 1 on finding the top k items."""

    def setUp(self):
        StatCounter.reset_counts()

    def test_top_k_select(self):
        """Tests the top_k_select function on a list of 1000 integers."""
        test_data = list(range(1000))
        random.shuffle(test_data)
        top_40, _ = top_k_select(test_data, 40)
        self.assertEqual(top_40, list(range(999, 959, -1)))

    def test_top_k_select_comparisons(self):
        """Tests the number of comparisons the top_k_select function makes
        on a list of 1000 integers.
        """
        test_data = list_of_keys(range(1000))
        random.shuffle(test_data)
        _, comparisons = top_k_select(test_data, 40)
        self.assertLess(comparisons, 40000)
        self.assertGreater(comparisons, 30000)

    def test_top_k_select_real_comparisons(self):
        """Tests the number of comparisons the top_k_select function makes
        on a list of 1000 integers.
        """
        test_data = list_of_keys(range(1000))
        random.shuffle(test_data)
        _, comparisons = top_k_select(test_data, 40)
        self.assertEqual(comparisons, real_comparisons(KEY_COMPS))

    def test_top_k_heap(self):
        """Tests the top_k_heap function on a list of 1000 integers."""
        test_data = list(range(1000))
        random.shuffle(test_data)
        top_40, _ = top_k_heap(test_data, 40)
        expected_top_40 = list(range(999, 959, -1))
        self.assertEqual(top_40, expected_top_40)

    def test_top_k_heap_comparisons(self):
        """Tests the number of comparisons made by the top_k_heap function
        on a list of 1000 integers.
        """
        test_data = list(range(1000))
        random.shuffle(test_data)
        _, comparisons = top_k_heap(test_data, 40)
        self.assertLess(comparisons, 10400)
        self.assertGreater(comparisons, 1040)

    def test_top_k_heap_real_comparisons(self):
        """Tests the number of comparisons made by the top_k_heap function
        on a list of 1000 integers.
        """
        test_data = list_of_keys(range(1000))
        random.shuffle(test_data)
        _, comparisons = top_k_heap(test_data, 40)
        self.assertEqual(comparisons, real_comparisons(KEY_COMPS))


class TestFastPriorityQueue(BaseTester):
    """Tests for Task 2 on fast heapify."""

    def test_fast_heapify_small(self):
        """Tests that heapify works on a small test case in sorted order."""
        fpq = FastPriorityQueue(list(range(10)))
        self.assertEqual(len(fpq), 10)
        self.assertEqual(fpq.validate(), True)

    def test_fast_heapify_random_data_small(self):
        """Tests that heapify works on a small test case in random order."""
        test_data = list(range(100))
        random.shuffle(test_data)
        fpq = FastPriorityQueue(test_data)
        self.assertEqual(len(fpq), 100)
        self.assertEqual(fpq.validate(), True)

    def test_fast_heapify_medium(self):
        """Tests that heapify works on a range of sizes - with sorted data"""
        max_depth = 16
        for size in [2**n for n in range(2, max_depth+1, 2)]:
            fpq = FastPriorityQueue(list(range(size)))
            self.assertEqual(len(fpq), size)
            self.assertEqual(fpq.validate(), True)

    def test_fast_heapify_random_data_medium(self):
        """Tests that heapify works on a range of sizes - with random data"""
        max_depth = 16
        for size in [2**n for n in range(2, max_depth+1, 2)]:
            test_data = list(range(1000))
            random.shuffle(test_data)
            fpq = FastPriorityQueue(test_data)
            self.assertEqual(len(fpq), 1000)
            self.assertEqual(fpq.validate(), True)

    # Your tests for testing the number of comparisons should go here if
    # you choose to use the unit testing framework.
    # Your code here is not marked not marked but we will check that
    # your FastPriorityQueue manages to heapify with O(n) key comparisons
    # and that your FastPriorityQueue counts any key comparisons correctly.


class TestFastPriorityQueueHugemongous(BaseTester):
    """Tests for Task 2 on fast heapify."""

    def test_fast_heapify_hugemongous(self):
        """Tests that heapify works on a range of sizes - with sorted data"""
        min_depth = 8
        max_depth = 12
        for size in [2**n for n in range(min_depth, max_depth+1, 2)]:
            fpq = FastPriorityQueue(list(range(size)))
            self.assertEqual(len(fpq), size)
            self.assertEqual(fpq.validate(), True)

    def test_fast_heapify_random_data_hugemongous(self):
        """Tests that heapify works on a range of sizes - with random data"""
        min_depth = 8
        max_depth = 12
        for size in [2**n for n in range(min_depth, max_depth+1, 2)]:
            test_data = list(range(1000))
            random.shuffle(test_data)
            fpq = FastPriorityQueue(test_data)
            self.assertEqual(len(fpq), 1000)
            self.assertEqual(fpq.validate(), True)


class TestChangePriorityQueue(BaseTester):
    """Tests for Task 3 on removing from a priority queue."""

    def test_cpq_heapify(self):
        """Tests that heapify still works correctly. Note this effectively
        tests whether swap items is swapping the items correctly and that
        the __init__ function has not been modified.
        """
        test_data = [str(digit) for digit in range(1000)]
        test_priorities = list_of_keys(list(range(1000)))
        random.shuffle(test_priorities)
        cpq = ChangePriorityQueue(test_data, test_priorities)
        self.assertEqual(len(cpq), 1000)
        self.assertEqual(cpq.validate(), True)

    def test_cpq_peek_max(self):
        """Tests the peek_max method on a small example."""
        cpq = ChangePriorityQueue()
        cpq.insert_with_priority('a', Key(1))
        cpq.insert_with_priority('b', Key(3))
        cpq.insert_with_priority('c', Key(8))
        cpq.insert_with_priority('d', Key(0))
        cpq.insert_with_priority('e', Key(4))
        self.assertEqual(cpq.peek_max(), 'c')

    def test_cpq_pop_max(self):
        """Tests the pop_max method on a small 7 item example."""
        test_priorities = list_of_keys([3, 67, 65, 8, 412, 1, 22])
        test_data = list(string.ascii_lowercase)[:len(test_priorities)]
        cpq = ChangePriorityQueue(test_data, test_priorities)
        self.assertEqual(len(cpq), 7)
        self.assertEqual(cpq._item_indices['g'], 6)
        self.assertEqual(cpq.pop_max(), 'e')
        self.assertEqual(len(cpq), 6)
        self.assertEqual(cpq._item_indices['g'], 1)
        self.assertEqual(cpq.validate(), True)

    def test_cpq_pop_max(self):
        """Tests the pop_max method on a small 7 item example."""
        test_priorities = list_of_keys([3, 67, 65, 8, 412, 1, 22])
        test_data = list(string.ascii_lowercase)[:len(test_priorities)]
        cpq = ChangePriorityQueue(test_data, test_priorities)
        self.assertEqual(len(cpq), 7)
        self.assertEqual(cpq._item_indices['g'], 6)
        # reset counters so only comparisons used during pop max are counted
        StatCounter.reset_counts()
        cpq.reset_comparisons()
        self.assertEqual(cpq.pop_max(), 'e')
        comparisons = cpq.get_comparisons()
        self.assertEqual(comparisons, real_comparisons(KEY_COMPS))
        self.assertEqual(len(cpq), 6)
        self.assertEqual(cpq._item_indices['g'], 1)
        self.assertEqual(cpq.validate(), True)

    def test_cpq_real_comps_insert_with_priority(self):
        """Tests the insert_with_priority method on a small example."""
        cpq = ChangePriorityQueue()
        cpq.insert_with_priority('a', Key(1))
        cpq.insert_with_priority('b', Key(3))
        cpq.insert_with_priority('c', Key(8))
        cpq.insert_with_priority('d', Key(0))
        cpq.insert_with_priority('e', Key(4))
        comparisons = cpq.get_comparisons()
        self.assertEqual(len(cpq), 5)
        self.assertEqual(cpq.validate(), True)
        self.assertEqual(comparisons, real_comparisons(KEY_COMPS))

    def test_cpq_remove_item(self):
        """Tests the remove_item method on a small 7 item example."""
        test_priorities = list_of_keys([3, 67, 65, 8, 412, 1, 22])
        test_data = list(string.ascii_lowercase)[:len(test_priorities)]
        cpq = ChangePriorityQueue(test_data, test_priorities)
        self.assertEqual(len(cpq), 7)
        self.assertEqual(cpq.pop_max(), 'e')
        self.assertEqual(len(cpq), 6)
        # reset counters so only comparisons used during pop max are counted
        StatCounter.reset_counts()
        cpq.reset_comparisons()
        self.assertEqual(cpq.remove_item('g'), 'g')
        comparisons = cpq.get_comparisons()
        self.assertEqual(comparisons, real_comparisons(KEY_COMPS))
        self.assertEqual(cpq.remove_item('g'), None)  # g no longer in heap
        self.assertEqual(cpq.remove_item(3), None)  # 3 isn't a value ...
        self.assertEqual(cpq.validate(), True)
        self.assertEqual(len(cpq), 5)
        self.assertEqual(cpq.pop_max(), 'b')
        self.assertEqual(cpq.validate(), True)
        self.assertEqual(cpq.pop_max(), 'c')
        self.assertEqual(cpq.validate(), True)
        # reset counters so only comparisons used during remove are counted
        StatCounter.reset_counts()
        cpq.reset_comparisons()
        self.assertEqual(cpq.remove_item('d'), 'd')
        comparisons = cpq.get_comparisons()
        self.assertEqual(comparisons, real_comparisons(KEY_COMPS))
        self.assertEqual(cpq.validate(), True)
        # reset counters so only comparisons used during remove are counted
        StatCounter.reset_counts()
        cpq.reset_comparisons()
        self.assertEqual(cpq.remove_item('d'), None)
        comparisons = cpq.get_comparisons()
        self.assertEqual(comparisons, real_comparisons(KEY_COMPS))
        self.assertEqual(cpq.validate(), True)
        self.assertEqual(len(cpq._item_indices), 2)
        self.assertEqual(cpq._item_indices['a'], 0)
        self.assertEqual(cpq._item_indices['f'], 1)
        self.assertEqual(cpq.validate(), True)


class TestDheapPriorityQueue(BaseTester):
    """Some tests for d-heaps. You should write some more, of course!"""

    def test_parent_index(self):
        """Tests whether the correct parent index is found with d=5."""
        dpq = DheapPriorityQueue(list_of_keys(range(100)), 5)
        self.assertEqual(dpq._parent_index(6), 1)
        self.assertEqual(dpq._parent_index(10), 1)
        self.assertEqual(dpq._parent_index(30), 5)
        # index 0 has no parent node.
        self.assertEqual(dpq._parent_index(0), -1)
        # 100 is not in the d-heap.
        self.assertEqual(dpq._parent_index(100), -1)

    def test_children_indices(self):
        """Tests whether the correct children indices are found with d=7."""
        dpq = DheapPriorityQueue(list_of_keys(range(100)), 7)
        self.assertEqual(sorted(dpq._children_indices(0)), list(range(1, 8)))
        self.assertEqual(sorted(dpq._children_indices(10)),
                         list(range(71, 78)))

    def test_heapify(self):
        """Tests whether heapify still works correctly in a large case with d=7."""
        dpq = DheapPriorityQueue(list_of_keys(range(10000)), 7)
        self.assertEqual(len(dpq), 10000)
        self.assertEqual(dpq.validate(), True)

    def test_insert_small_d6(self):
        """Tests whether insert still works correctly with a few items and d=6."""
        dpq = DheapPriorityQueue(branch_factor=6)
        for key in list_of_keys([5, 4, 6, 3, 2, 7]):
            dpq.insert(key)
            self.assertEqual(dpq.validate(), True)
        self.assertEqual(len(dpq), 6)
        self.assertEqual(dpq.validate(), True)

    def test_insert_medium_d6(self):
        """Tests whether insert still works correctly with a few items and d=6."""
        dpq = DheapPriorityQueue(branch_factor=6)
        test_data = list_of_keys(range(1000))
        random.shuffle(test_data)
        for item in test_data:
            dpq.insert(item)
            self.assertEqual(dpq.validate(), True)
        self.assertEqual(len(dpq), 1000)

    def test_insert_large_d6(self):
        """Tests whether insert still works correctly with a few items and d=6."""
        d = 6
        n_items = 2048
        dpq = DheapPriorityQueue(branch_factor=d)
        test_data = list_of_keys(range(n_items))
        random.shuffle(test_data)
        for item in test_data:
            dpq.insert(item)
            self.assertEqual(dpq.validate(), True)
        self.assertEqual(len(dpq), n_items)

    def test_pop_max_small(self):
        """Tests whether pop_max still works correctly in a small case with d=3."""
        dpq = DheapPriorityQueue(list_of_keys([3, 67, 65, 8, 412, 1, 22]), 3)
        self.assertEqual(len(dpq), 7)
        self.assertEqual(dpq.pop_max(), Key(412))
        self.assertEqual(len(dpq), 6)
        self.assertEqual(dpq.validate(), True)

    def test_pop_max_medium(self):
        """Tests whether pop_max still works correctly in a medium case with d=13."""
        start_data = list_of_keys((range(1000)))
        random.shuffle(start_data)
        dpq = DheapPriorityQueue(start_data, 13)
        for item in list_of_keys(range(999, 800, -1)):
            self.assertEqual(dpq.pop_max(), item)
            self.assertEqual(dpq.validate(), True)
        self.assertEqual(len(dpq), 801)
        self.assertEqual(dpq.validate(), True)

    def test_pop_max_large(self):
        """Tests whether pop_max still works correctly in a large case with d=13."""
        dpq = DheapPriorityQueue(list_of_keys(range(10000)), 13)
        for item in list_of_keys(range(9999, 8000, -1)):
            self.assertEqual(dpq.pop_max(), item)
            self.assertEqual(dpq.validate(), True)
        self.assertEqual(len(dpq), 8001)
        self.assertEqual(dpq.validate(), True)




def all_tests_suite():
    """Returns a unit_test suite containing all desired tests."""
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestTopK))
    suite.addTest(unittest.makeSuite(TestChangePriorityQueue))
    suite.addTest(unittest.makeSuite(TestDheapPriorityQueue)) 
    suite.addTest(unittest.makeSuite(TestFastPriorityQueue))
    suite.addTest(unittest.makeSuite(TestFastPriorityQueueHugemongous))
    
    
    return suite


def main():
    """Runs all tests returned by all_tests_suite()."""
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_runner.run(all_tests_suite())


if __name__ == '__main__':
    main()
