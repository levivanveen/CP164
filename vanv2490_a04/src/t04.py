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
from functions import pq_split_key


source = Priority_Queue()
source.insert(5)
source.insert(3)
source.insert(8)
source.insert(1)
key = 4

target1, target2 =pq_split_key(source, key)


while target1.is_empty() == False:
    print('target1: {}'.format(target1.remove()))
while target2.is_empty() == False:
    print('target2: {}'.format(target2.remove()))
print('key: {}'.format(key))