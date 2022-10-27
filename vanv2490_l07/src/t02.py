"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Levi Van Veen
ID: 200852490
Email: vanv2490@mylaurier.ca
__updated__ = "2021-03-10"
-------------------------------------------------------
"""
# Imports
from List_linked import List

lst_1 = List()

lst_1.append(99)
for v in lst_1:
    print(v)


lst_2 = List()
lst_2.append(33)
lst_2.append(66)
lst_2.append(22)
lst_2.append(55)
lst_2.append(11)
lst_2.append(44)
for v in lst_2:
    print(v)


print(lst_1.is_identical_r(lst_2))