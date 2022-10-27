"""
-------------------------------------------------------
[Assignment 2, Task 1]
-------------------------------------------------------
Author: Levi Van Veen
ID: 200852490
Email: vanv2490@mylaurier.ca
__updated__ = "2021-01-27"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import get_by_year, read_movies

fv = open("movies.txt", 'r')
movies = read_movies(fv)


    
year = int(input("Enter year: "))

ymovies = get_by_year(movies, year)

for v in ymovies:
    print(v)
    print()