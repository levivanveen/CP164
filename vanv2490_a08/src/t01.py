"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Levi Van Veen
ID: 200852490
Email: vanv2490@mylaurier.ca
__updated__ = "2021-03-25"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST

bst = BST()
bst.insert(99)
bst.insert(88)

bst.insert(11)
bst.insert(5)
bst.insert(13)
bst.insert(12)
bst.insert(20)
bst.insert(18)
bst.insert(22)
bst.insert(4)



bst.remove(11)

for v in bst:
    print('{},'.format(v))
a = bst.inorder()
print()
for v in a:
    print(v)