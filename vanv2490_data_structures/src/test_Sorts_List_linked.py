"""
-------------------------------------------------------
Tests various linked sorting functions.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 C
__updated__ = "2021-03-31"
-------------------------------------------------------
"""
# Imports
import random

from List_linked import List
from Number import Number
from Sorts_List_linked import Sorts

# Constants
SIZE = 100  # Size of array to sort.
XRANGE = 1000  # Range of values in random arrays to sort.
TESTS = 100  # Number of random arrays to generate.

SORTS = (
    ('Bubble Sort', Sorts.bubble_sort),
    ('Insertion Sort', Sorts.insertion_sort),
    ('Merge Sort', Sorts.merge_sort),
    ('Quick Sort', Sorts.quick_sort),
    ('Selection Sort', Sorts.selection_sort),
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted List of Number objects.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """
    values = List()
    for v in range(SIZE):
        values.insert(101, Number(v))
    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed List of Number objects.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """
    values = List()
    reversing = range(SIZE - 1, -1, -1)
    for v in reversing:
        values.insert(101, Number(v))
    return values


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        lists - TEST lists of SIZE Number objects containing
            values between 0 and XRANGE (list of List of Number)
    -------------------------------------------------------
    """
    lists = []
    for _ in range(TESTS):
        lists.append(List())
    for lst in lists:
        for _ in range(SIZE):
            lst.insert(0, Number(random.randrange(XRANGE)))

    return lists


def test_sort(title, func):
    """
    -------------------------------------------------------
    Tests a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of Lists in random order.
    Use: test_sort(title, func)
    -------------------------------------------------------
    Parameters:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Returns:
        None
    -------------------------------------------------------
    """
    Sorts.swaps = 0
    Number.comparisons = 0
    values_sorted = create_sorted()
    func(values_sorted)
    swaps_sorted = Sorts.swaps
    comparison_sorted = values_sorted[0].comparisons

    Sorts.swaps = 0
    Number.comparisons = 0

    values_reversed = create_reversed()

    func(values_reversed)
    swaps_reversed = Sorts.swaps
    comparison_reversed = values_reversed[0].comparisons

    Sorts.swaps = 0
    Number.comparisons = 0
    swaps_random = 0
    values_random = create_randoms()
    for v in values_random:
        func(v)

    swaps_random = Sorts.swaps

    swaps_random = swaps_random // len(values_random)

    comparison_random = Number.comparisons // len(values_random)

    print('n:   {}       |      Comparisons       | |         Swaps           |'.format(
        len(values_sorted)))
    print('Algorithm      In Order Reversed   Random In Order Reversed   Random')
    print('-------------- -------- -------- -------- -------- -------- --------')
    print('{:<14}{:>9}{:>9}{:>9}{:>9}{:>9}{:>9}'.format(title, int(comparison_sorted),
                                                        int(comparison_reversed), comparison_random, int(swaps_sorted), int(swaps_reversed), int(swaps_random)))
    print()
    return
