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
from Priority_Queue_linked import Priority_Queue

queue1 = Priority_Queue()
queue2 = Priority_Queue()

queue1.insert(1)
queue1.insert(4)
queue1.insert(11)
queue1.insert(44)

queue2.insert(1)
queue2.insert(4)
queue2.insert(11)
queue2.insert(44)

target = Priority_Queue()

target.combine(queue1, queue2)
for v in target:
    print(v)