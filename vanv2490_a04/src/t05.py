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
from Priority_Queue_array import Priority_Queue

source = Priority_Queue()
source.insert(5)
source.insert(1)
source.insert(10)
source.insert(8)

key = 6
target1, target2 = source.split_key(key)

while target1.is_empty() == False:
    print('target1: {}'.format(target1.remove()))
while target2.is_empty() == False:
    print('target2: {}'.format(target2.remove()))
print('key: {}'.format(key))