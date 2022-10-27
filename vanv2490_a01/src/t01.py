"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Levi Van Veen
ID: 200852490
Email: vanv2490@mylaurier.ca
__updated__ = "2021-01-21"
-------------------------------------------------------
"""
# Imports
from functions import is_leap_year

year = int(input("Enter a year to be checked: "))

leap_year = is_leap_year(year)

if leap_year == True:
    print("{} is a leap year".format(year))
else:
    print("{} is not a leap year".format(year))
