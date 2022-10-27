"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Levi Van Veen
ID: 200852490
Email: vanv2490@mylaurier.ca
__updated__ = "2021-04-01"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST

bst = BST()
bst.insert(12)
bst.insert(18)
bst.insert(15)
bst.insert(31)
bst.insert(11)
bst.insert(20)
bst.insert(103)

zero, one, two = bst.node_counts()
print(zero, one, two)

print(13 in bst)

print(bst.parent(18))
print(bst.parent(20))
