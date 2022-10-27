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
from List_linked import List
lst = List()
lst.append(5)
print(lst.find(5))
print(lst.index(5))
print(lst.__contains__(5))
lst.append(8)
print(lst.max())
print(lst.min())
