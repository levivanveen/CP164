"""
-------------------------------------------------------
[Assignment 2, Task 3]
-------------------------------------------------------
Author: Levi Van Veen
ID: 200852490
Email: vanv2490@mylaurier.ca
__updated__ = "2021-01-27"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import get_by_genre, read_movies

fv = open("movies.txt", 'r')
movies = read_movies(fv)


    
genre = int(input("Enter genre: "))

gmovies = get_by_genre(movies, genre)

for v in gmovies:
    print(v)
    print()