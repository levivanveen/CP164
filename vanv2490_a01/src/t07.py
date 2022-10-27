"""
-------------------------------------------------------
[Assignment 1, Task 7]
-------------------------------------------------------
Author: Levi Van Veen
ID: 200852490
Email: vanv2490@mylaurier.ca
__updated__ = "2021-01-21"
-------------------------------------------------------
"""
# Imports
from functions import substitute

fv = open("pelee.txt")
sub = open("substitute.txt", 'w')
ciphertext = 'DAVIBROWNZCEFGHJKLMPQSTUXY'

for line in fv:
    string = line
    estring = substitute(string, ciphertext)
    sub.write(estring) 

fv.close()
sub.close()