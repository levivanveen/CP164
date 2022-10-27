"""
-------------------------------------------------------
[Assignment 2, Task 4]
-------------------------------------------------------
Author: Levi Van Veen
ID: 200852490
Email: vanv2490@mylaurier.ca
__updated__ = "2021-01-27"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import get_by_genres, read_movies

fv = open("movies.txt", 'r')
movies = read_movies(fv)


genres = [3,4]
print("genres: {}".format(genres))
gmovies = get_by_genres(movies, genres)

for v in gmovies:
    print(v)
    print()