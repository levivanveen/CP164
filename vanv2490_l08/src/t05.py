"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Levi Van Veen
ID: 200852490
Email: vanv2490@mylaurier.ca
__updated__ = "2021-03-17"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
from morse import ByLetter, fill_letter_bst, encode_morse, decode_morse, fill_code_bst, ByCode

var1 = ByLetter('E', None)
var2 = ByLetter('L', None)
print(var1 == var2)

var3 = ByCode(None, '--')
var4 = ByCode(None, '--.')
print(var3 < var4)

bst1 = BST()
bst2 = BST()

data2 = (('M', '--'), ('F', '..-.'), ('T', '-'),
         ('C', '-.-.'), ('J', '.---'), ('P', '.--.'),
         ('W', '.--'), ('A', '.-'), ('D', '-..'),
         ('H', '....'), ('K', '-.-'), ('N', '-.'),
         ('R', '.-.'), ('U', '..--'), ('Y', '-.--'),
         ('B', '-...'), ('E', '.'), ('I', '..'),
         ('G', '--.'), ('L', '.-..'), ('O', '---'),
         ('Q', '--.-'), ('S', '...'), ('V', '...-'),
         ('X', '-..-'), ('Z', '--..'))
fill_code_bst(bst2, data2)
fill_letter_bst(bst1, data2)
text = "Levi is"
code = '.-.. . ...- .. .. ...'

decoded = decode_morse(bst2, code)


encoded = encode_morse(bst1, text)
