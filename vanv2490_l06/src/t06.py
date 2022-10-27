"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Levi Van Veen
ID: 200852490
Email: vanv2490@mylaurier.ca
__updated__ = "2021-02-10"
-------------------------------------------------------
"""
# Imports
from utilities import array_to_list, list_to_array
from List_array import List

source = [4,3,1,6,4]
llist = List()
array_to_list(llist, source)
print(source)
for v in llist:
    print(v)

list_to_array(llist, source)
print(source)
print(llist.is_empty())