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
from List_array import List

lst = List()

lst.append(5)
lst.append(6)
print(lst.__getitem__(1))
lst.__setitem__(1, 1)
print(lst.__getitem__(1))