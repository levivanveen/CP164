"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Levi Van Veen
ID: 200852490
Email: vanv2490@mylaurier.ca
__updated__ = "2021-04-20"
-------------------------------------------------------
"""
# Imports
from Hash_Set_array import Hash_Set

hs = Hash_Set(7)
ht = Hash_Set(7)
ht.insert(55)
hs.insert(55)
print(hs.is_identical(ht))
