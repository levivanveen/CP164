"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Levi Van Veen
ID: 200852490
Email: vanv2490@mylaurier.ca
__updated__ = "2021-01-27"
-------------------------------------------------------
"""
# Imports
from utilities import stack_test
from Movie_utilities import read_movies

fv = open("movies.txt", 'r')
source = read_movies(fv)

stack_test(source)
