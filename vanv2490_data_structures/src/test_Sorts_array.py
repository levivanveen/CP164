"""
-------------------------------------------------------
Tests various array-based sorting functions.
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
from Number import Number
from Sorts_array import Sorts

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
    ('Bin. Ins. Sort', Sorts.binary_insert_sort),
    ('BST Sort', Sorts.bst_sort),
    ('Cocktail Sort', Sorts.cocktail_sort),
    ('Comb Sort', Sorts.comb_sort),
    ('Heap Sort', Sorts.heap_sort),
    ('Shell Sort', Sorts.shell_sort)
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted list of SIZE Number objects with values
        from 0 up to SIZE-1.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """
    values = []
    for v in range(SIZE):
        target = Number(v)
        values.append(target)

    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed list of SIZE Number objects with values
        from SIZE-1 down to 0.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """
    values = []
    reversing = range(SIZE - 1, -1, -1)
    for v in reversing:
        target = Number(v)
        values.append(target)

    return values


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects with TEST rows and
    SIZE columns of values between 0 and XRANGE.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        arrays - TEST lists of SIZE Number objects containing
            values between 0 and XRANGE (list of list of Number)
    -------------------------------------------------------
    """
    arrays = []
    for _ in range(TESTS):
        arrays.append([])
    for lst in arrays:
        for _ in range(SIZE):
            lst.append(Number(random.randrange(XRANGE)))

    return arrays


def test_sort(title, func):
    """
    -------------------------------------------------------
    Test a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of arrays in random order.
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
