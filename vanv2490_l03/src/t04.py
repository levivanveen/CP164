"""
-------------------------------------------------------
[Lab 3, Task 4]
-------------------------------------------------------
Author: Levi Van Veen
ID: 200852490
Email: vanv2490@mylaurier.ca
__updated__ = "2021-02-03"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue

q = Priority_Queue()

value = 15
q.insert(value)
value = 12
q.insert(value)
print(q.peek())
print(q.remove())
q.insert(8)