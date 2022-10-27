"""
-------------------------------------------------------
[Assignment 2, Task 2]
-------------------------------------------------------
Author: Levi Van Veen
ID: 200852490
Email: vanv2490@mylaurier.ca
__updated__ = "2021-01-27"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import get_by_rating, read_movies
from Movie import Movie

fv = open("movies.txt", 'r')
movies = read_movies(fv)


    
rating = float(input("Enter rating between 0 and 10: "))
while rating < Movie.MIN_RATING or rating > Movie.MAX_RATING:
    rating = float(input("Enter rating between 0 and 10: "))

rmovies = get_by_rating(movies, rating)

for v in rmovies:
    print(v)
    print()