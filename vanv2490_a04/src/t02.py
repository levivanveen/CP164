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
from functions import queue_is_identical

source1 = Queue(3)
source2 = Queue(2)

source1.insert(99)
print('Added 4 to source 1')

print('Added 3 to source 1')

print()



identical = queue_is_identical(source1, source2)

if identical:
    print("Both queue's are identical")
else:
    print("The queue's are not identical")