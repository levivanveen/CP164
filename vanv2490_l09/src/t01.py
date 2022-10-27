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
from functions import hash_table
from Movie_utilities import read_movies

fv = open('movies.txt', 'r')

a = read_movies(fv)
hash_table(5, a)

fv.close()
