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
from Sorts_Deque_linked import Sorts
from Deque_linked import Deque

a = Deque()
a.insert_rear(0)
a.insert_rear(0)
a.insert_rear(0)

Sorts.gnome_sort(a)
for v in a:
    print(v)
