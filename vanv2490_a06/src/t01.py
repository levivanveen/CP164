"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Levi Van Veen
ID: 200852490
Email: vanv2490@mylaurier.ca
__updated__ = "2021-03-11"
-------------------------------------------------------
"""
# Imports
from List_linked import List
from Movie_utilities import read_movies

fv = open('movies.txt', 'r')
movies = read_movies(fv)

lst = List()
fst = List()
source1 = List()

for v in range(5):
    lst.append(v)


for v in range(6):
    fst.append(v)
for v in lst:
    print(v)
print()

target1, target2 = lst.split_th()
for v in target1:
    print('target1 {}'.format(v))
print()
for v in target2:
    print('target2 {}'.format(v))
    