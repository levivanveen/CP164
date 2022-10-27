"""
-------------------------------------------------------
[Assignment 1, Task 5]
-------------------------------------------------------
Author: Levi Van Veen
ID: 200852490
Email: vanv2490@mylaurier.ca
__updated__ = "2021-01-21"
-------------------------------------------------------
"""
# Imports
from functions import file_analyze

fv = open("task_5.txt")

u, l, d, w, r = file_analyze(fv)

print("The file has {} uppercase characters".format(u))
print("The file has {} lowercase characters".format(l))
print("The file has {} digit characters".format(d))
print("The file has {} whitespace characters".format(w))
print("The file has {} other characters".format(r))

fv.close()