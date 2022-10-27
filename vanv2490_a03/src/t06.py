"""
-------------------------------------------------------
[Assignment 3, Task 6]
-------------------------------------------------------
Author: Levi Van Veen
ID: 200852490
Email: vanv2490@mylaurier.ca
__updated__ = "2021-02-04"
-------------------------------------------------------
"""
# Imports
from functions import reroute

opstring = 'SXXSSXSX'
values_in = [1,2,3,4]

values_out = reroute(opstring, values_in)

print('values in: {}'.format(values_in))
print('opstring: {}'.format(opstring))
print('values out: {}'.format(values_out))