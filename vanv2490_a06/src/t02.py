"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Levi Van Veen
ID: 200852490
Email: vanv2490@mylaurier.ca
__updated__ = "2021-03-11"
-------------------------------------------------------
"""
# Imports
from Sorted_List_linked import Sorted_List

sorted = Sorted_List()

sorted.insert(27)
sorted.insert(5)
sorted.insert(5)
sorted.insert(27)
sorted.insert(61)

sorted2 = Sorted_List()
sorted2.insert(5)
sorted2.insert(5)
sorted2.insert(27)
sorted2.insert(61)

target = Sorted_List()


target.intersection(sorted, sorted2)

for v in target:
    print(v)