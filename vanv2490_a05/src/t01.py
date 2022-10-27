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
from List_array import List
from Movie import Movie

list1 = List()
list2 = List()

list1.append(2)
list1.append(2)
list1.append(2)
list1.append(2)
list1.append(3)

list2.append(3)

list3 = List()
list3.intersection(list1, list2)
print(len(list3))