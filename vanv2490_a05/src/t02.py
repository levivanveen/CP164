"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Levi Van Veen
ID: 200852490
Email: vanv2490@mylaurier.ca
__updated__ = "2021-02-25"
-------------------------------------------------------
"""
# Imports
from Sorted_List_array import Sorted_List
from Movie import Movie

sorted = Sorted_List()

source1 = Sorted_List()
source1.insert(4)
source1.insert(10)
source1.insert(6)
source1.insert(6)

target1, target2 = source1.split_key(6)
print(len(target1))
print(len(target2))