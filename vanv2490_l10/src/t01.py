"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Levi Van Veen
ID: 200852490
Email: vanv2490@mylaurier.ca
__updated__ = "2021-03-31"
-------------------------------------------------------
"""
# Imports
from test_Sorts_List_linked import create_reversed, create_sorted, create_randoms, test_sort
from Sorts_array import Sorts

test_sort('Bubble Sort', Sorts.bubble_sort)
test_sort('Comb Sort', Sorts.comb_sort)
test_sort('Insertion Sort', Sorts.insertion_sort)
test_sort('Merge Sort', Sorts.binary_insert_sort)
test_sort('Quick Sort', Sorts.quick_sort)
test_sort('Selection Sort', Sorts.selection_sort)
