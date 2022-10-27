"""
-------------------------------------------------------
[Lab 1 testing]
-------------------------------------------------------
Author: Levi Van Veen
ID: 200852490
Email: vanv2490@mylaurier.ca
__updated__ = "2021-01-20"
-------------------------------------------------------
"""
# Imports
from Movie import Movie
from Movie_utilities import read_movies, read_genres, get_movie

fv = open("movies.txt", 'r')
movies = read_movies(fv)

for v in movies:
    print(v)
    
genres = read_genres()

movie = get_movie()

fv.close()