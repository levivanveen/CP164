"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Levi Van Veen
ID: 200852490
Email: vanv2490@mylaurier.ca
__updated__ = "2021-02-10"
-------------------------------------------------------
"""
# Imports
from utilities import list_test
from Movie_utilities import read_movies

fv = open('movies.txt')

a = read_movies(fv)

list_test(a)
fv.close()


