"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Levi Van Veen
ID: 200852490
Email: vanv2490@mylaurier.ca
__updated__ = "2021-03-24"
-------------------------------------------------------
"""
# Imports
from Hash_Set_array import Hash_Set


hs = Hash_Set(2)

for v in range(35):
    hs.insert(v)
hs.debug()

print()

for v in range(10):
    hs.insert(v)

print("REHASH")
hs.debug()
