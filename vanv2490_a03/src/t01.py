"""
-------------------------------------------------------
[Assignment 3, Task 1]
-------------------------------------------------------
Author: Levi Van Veen
ID: 200852490
Email: vanv2490@mylaurier.ca
__updated__ = "2021-02-04"
-------------------------------------------------------
"""
# Imports
from functions import stack_split_alt
from Stack_array import Stack

a = [5,7,8,9,12,14,8]
print('Source {}'.format(a))
print()

source = Stack()

for v in a:
    source.push(v)
    
target1, target2 = stack_split_alt(source)

while target1.is_empty() == False:
    print('target1 {}'.format(target1.pop()))
print()
while target2.is_empty() == False:
    print('target2 {}'.format(target2.pop()))
