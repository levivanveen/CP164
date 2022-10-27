"""
-------------------------------------------------------
[Assignment 2, Task 5]
-------------------------------------------------------
Author: Levi Van Veen
ID: 200852490
Email: vanv2490@mylaurier.ca
__updated__ = "2021-01-27"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import genre_counts, read_movies

fv = open("movies.txt", 'r')
movies = read_movies(fv)

counts = genre_counts(movies)

print(counts)