"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Levi Van Veen
ID: 200852490
Email: vanv2490@mylaurier.ca
__updated__ = "2021-02-11"
-------------------------------------------------------
"""
# Imports
from Queue_circular import Queue

queue = Queue(3)
queue.insert(23)
print(queue.__len__())
queue.insert(3)
print(queue.__len__())
print(queue.remove())
print(queue.__len__())
queue.insert(6)
print(queue.__len__())
queue.insert(7)

for v in queue:
    print(v)
print(queue.__len__())
print(queue.is_empty())
print(queue.is_full())
print(queue.remove())
print(queue.__len__())
print(queue.remove())
print(queue.__len__())
print(queue.peek())
print(queue.remove())