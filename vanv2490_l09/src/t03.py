"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Levi Van Veen
ID: 200852490
Email: vanv2490@mylaurier.ca
__updated__ = "2021-04-20"
-------------------------------------------------------
"""
# Imports
from Hash_Set_array import Hash_Set
from Movie_utilities import read_movies

fv = open('movies.txt', 'r')
hs = Hash_Set(7)
a = read_movies(fv)

for v in a:
    hs.insert(v)
hs.debug()

fv.close()
