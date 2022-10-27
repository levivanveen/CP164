"""
-------------------------------------------------------
[]
-------------------------------------------------------
Author: Levi Van Veen
ID: 200852490
Email: vanv2490@mylaurier.ca
__updated__ = "2021-04-19"
-------------------------------------------------------
"""
# Imports
from Sorted_List_linked import Sorted_List

a = Sorted_List()
b = Sorted_List()
a.insert(11)
a.insert(33)
a.insert(55)
a.insert(75)

new_list = a.copy_r()

for v in new_list:
    print(v)
