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
#Imports
from Queue_linked import Queue

queue1 = Queue()
queue2 = Queue()

queue1.insert(1)
queue1.insert(4)
queue1.insert(11)
queue1.insert(44)

queue2.insert(1)
queue2.insert(4)
queue2.insert(11)
queue2.insert(44)

target1, target2 = queue1.split_alt()

for v in target1:
    print(v)

print()

for v in target2:
    print(v)

