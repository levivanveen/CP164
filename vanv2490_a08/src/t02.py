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
from Letter import Letter
from BST_linked import BST
from functions import do_comparisons, comparison_total, letter_table

SEP = '-' * 60

DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

bst1 = BST()
bst2 = BST()
bst3 = BST()

for v in DATA1:
    v = Letter(v)
    bst1.insert(v)

for v in DATA2:
    v = Letter(v)
    bst2.insert(v)

for v in DATA3:
    v = Letter(v)
    bst3.insert(v)

fv = open('miserables.txt', 'r')

do_comparisons(fv, bst1)

total = comparison_total(bst1)

print('Comparing by order: {}'.format(DATA1))
print('Total Comparisons: {:,}'.format(total))
print(SEP)

fv = open('miserables.txt', 'r')


do_comparisons(fv, bst2)

total2 = comparison_total(bst2)

print('Comparing by order: {}'.format(DATA2))
print('Total Comparisons: {:,}'.format(total2))
print(SEP)

fv = open('miserables.txt', 'r')


do_comparisons(fv, bst3)

total3 = comparison_total(bst3)

print('Comparing by order: {}'.format(DATA3))
print('Total Comparisons: {:,}'.format(total3))
print(SEP)

letter_table(bst1)
letter_table(bst2)
letter_table(bst3)
