"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Levi Van Veen
ID: 200852490
Email: vanv2490@mylaurier.ca
__updated__ = "2021-01-21"
-------------------------------------------------------
"""
# Imports
from functions import matrixes_multiply

a = [[1,4],[2,3],[3,2],[4,1]]
b = [[3,1,3,2],[2,2,1,3],[1,3,2,1]]

c = matrixes_multiply(a, b)

print(c)