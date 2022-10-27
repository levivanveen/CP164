"""
-------------------------------------------------------
[Assignment 1, Task 8]
-------------------------------------------------------
Author: Levi Van Veen
ID: 200852490
Email: vanv2490@mylaurier.ca
__updated__ = "2021-01-21"
-------------------------------------------------------
"""
# Imports
from functions import shift

fv = open("pelee.txt")
file = open("shift.txt", 'w')
n = 125
for line in fv:
    string = line
    estring = shift(string, n)
    file.write(estring)






fv.close()
file.close()