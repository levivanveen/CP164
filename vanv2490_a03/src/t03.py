"""
-------------------------------------------------------
[Assignment 3, Task 3]
-------------------------------------------------------
Author: Levi Van Veen
ID: 200852490
Email: vanv2490@mylaurier.ca
__updated__ = "2021-02-04"
-------------------------------------------------------
"""
# Imports
from functions import stack_reverse
from Stack_array import Stack

a = [1,2,3,4,5,6,7,8,9]
source = Stack()
print(a)
for v in a:
    source.push(v)

stack_reverse(source)

while source.is_empty() == False:
    print(source.pop())

