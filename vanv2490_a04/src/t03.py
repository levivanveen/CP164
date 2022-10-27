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


target = Queue(4)
source = Queue(4)

target.insert(2)
target.insert(3)


source.insert(2)
source.insert(3)
source.insert(3)

print(source.is_identical(target))