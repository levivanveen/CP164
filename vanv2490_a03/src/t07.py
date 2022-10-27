"""
-------------------------------------------------------
[Assignment 3, Task 7]
-------------------------------------------------------
Author: Levi Van Veen
ID: 200852490
Email: vanv2490@mylaurier.ca
__updated__ = "2021-02-04"
-------------------------------------------------------
"""
# Imports
from functions import is_mirror_stack
from enum import Enum

# Enumerated constant
MIRRORED = Enum('MIRRORED',
                {'IS_MIRRORED': "is a mirror", 'TOO_MANY_LEFT': "too many characters in L",
                 'TOO_MANY_RIGHT': "too many characters in R", 'MISMATCHED': "L and R don't match",
                 'INVALID_CHAR': "invalid character", 'NOT_MIRRORED': "no mirror character"})

string = 'assdamdsa'
valid_chars = 'asd'
m = 'm'

mirror = is_mirror_stack(string, valid_chars, m)
print('String: {}'.format(string))
print("Valid Characters: {}".format(valid_chars))
print('Mirror letter: {}'.format(m))
print("Mirror: {}".format(mirror.value))