"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Levi Van Veen
ID: 200852490
Email: vanv2490@mylaurier.ca
__updated__ = "2021-02-03"
-------------------------------------------------------
"""
# Imports
from utilities import priority_queue_test
from Movie_utilities import read_movies

fv = open('movies.txt', 'r')
a = read_movies(fv)

priority_queue_test(a)

