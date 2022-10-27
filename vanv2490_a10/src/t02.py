"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Levi Van Veen
ID: 200852490
Email: vanv2490@mylaurier.ca
__updated__ = "2021-04-08"
-------------------------------------------------------
"""
# Imports
from Sorts_List_linked import Sorts
from List_linked import List

a = List()
a.append(0)
a.append(0)
a.append(0)


Sorts.radix_sort(a)

for v in a:
    print(v)
