"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Levi Van Veen
ID: 200852490
Email: vanv2490@mylaurier.ca
__updated__ = "2021-03-18"
-------------------------------------------------------
"""
# Imports
from Deque_linked import Deque

deque = Deque()

deque.insert_front(3)
deque.insert_rear(5)
deque.insert_front(1)
deque.insert_rear(11)
deque.insert_rear(25)
for v in deque:
    print(v)

deque._swap(deque._front, deque._front)
print()
for v in deque:
    print(v)

deque._swap(deque._front, deque._rear)
print()
for v in deque:
    print(v)

deque._swap(deque._front, deque._front._next)
print()
for v in deque:
    print(v)

deque._swap(deque._rear._prev, deque._rear)
print()
for v in deque:
    print(v)

deque._swap(deque._front._next, deque._rear._prev)
print()
for v in deque:
    print(v)
    
deque._swap(deque._front._next, deque._rear)
print()
for v in deque:
    print(v)

deque._swap(deque._rear._prev, deque._front)
print()
for v in deque:
    print(v)
