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
lst.insert(0,4)

lst.append(5)
lst.append(6)
lst.append(7)
lst.insert(-1,3)
#lst.remove(3)
for v in lst:
    print(v)
