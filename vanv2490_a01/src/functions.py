"""
-------------------------------------------------------
[Assignment 1, functions]
-------------------------------------------------------
Author: Levi Van Veen
ID: 200852490
Email: vanv2490@mylaurier.ca
__updated__ = "2021-01-21"
-------------------------------------------------------
"""
# Imports

# Constants
VOWELS = 'AaEeOoIiUU'
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def is_leap_year(year):
    """
    -------------------------------------------------------
    Leap year determination.
    Use: leap_year = is_leap_year(year)
    -------------------------------------------------------
    Parameters:
        year - year to determine if it is a leap year (int > 0)
    Returns:
        leap_year - True if year is a leap year, False otherwise (boolean)
    -------------------------------------------------------
    """
    leap_year = True
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 != 0:
                leap_year = False
    else:
        leap_year = False
    return leap_year

def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """
    check_list = []
    i = 0
    
    while i < len(values):
        if (values[i] in check_list) == False:
            check_list.append(values[i])
            i += 1
        else:
            values.pop(i)
    return

def matrix_transpose(a):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    Use: b = matrix_transpose(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (list of lists of ?)
    Returns:
        b - the transposed matrix (list of lists of ?)
    -------------------------------------------------------
    """
    b = []
    row = len(a)
    column = len(a[0])
    i = 0
    j = 0 
    while i < column:
        b.append([])
        j = 0
        while j < row:
            b[i].append(a[j][i])
            j += 1
        i += 1
    return b        
    
def matrixes_multiply(a, b):
    """
    -------------------------------------------------------
    Multiplies the contents of matrixes a and b.
    If a is mxn in size, and b is nxp in size, then c is mxp.
    a and b must be unchanged.
    Use: c = matrixes_multiply(a, b)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
        b - a 2D list (2D list of int/float)
    Returns:
        c - the matrix multiple of a and b (2D list of int/float)
    -------------------------------------------------------
    """
    c = []
    c_entry = 0
    a_row = len(a)
    a_column = len(a[0])
    b_row = len(b)
    b_column = len(b[0])
    
    if a_row == b_column:
        for i in range(a_column):
            c.append([])
        for r in range(b_row):    
            for i in range(a_column):
                c_entry = 0
                for j in range(a_row):
                    c_entry += a[j][i] * b[r][j]
                c[i].append(c_entry)
    return c
    
    
    
def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged.
    Use: u, l, d, w, r = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        u - the number of uppercase letters in the file (int)
        l - the number of lowercase letters in the file (int)
        d - the number of digits in the file (int)
        w - the number of whitespace characters in the file (int)
        r - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    u = 0
    l = 0
    d = 0
    w = 0
    r = 0
    
    for line in fv:
        #string = line
        for ch in line:
            if ch.isdigit():
                d += 1
            elif ch.isalpha():
                if ch.isupper():
                    u += 1
                else:
                    l += 1
            elif ch.isspace():
                w += 1
            else:
                r += 1
        
    return u, l, d, w, r
    
def dsmvwl(s):
    """
    -------------------------------------------------------
    Disemvowels a string. out contains all the characters in s
    that are not vowels. ('y' is not considered a vowel.) Case is preserved.
    Use: out = dsmvl(s)
    -------------------------------------------------------
    Parameters:
       s - a string (str)
    Returns:
       out - s with the vowels removed (str)
    -------------------------------------------------------
    """
    out = ''
    for ch in s:
        if (ch in VOWELS) == False:
            out += ch
    return out
    
def substitute(string, ciphertext):
    """
    -------------------------------------------------------
    Encipher a string using the letter positions in ciphertext.
    Only letters are enciphered, and the returned string is
    in upper case.
    Use: estring = substitute(string, ciphertext):
    -------------------------------------------------------
    Parameters:
        string - string to encipher (str)
        ciphertext - ciphertext alphabet (str)
    Returns:
        estring - the enciphered string (str)
    -------------------------------------------------------
    """
    upper_string = string.upper()
    estring = ''
    i = 0
    j = 0
    while i < len(upper_string):
        if upper_string[i].isalpha():
            j = 0
            while upper_string[i] != ALPHABET[j]:
                j += 1
            estring += ciphertext[j]
        else:
            estring += upper_string[i]
        i += 1
    return estring


def shift(string, n):
    """
    -------------------------------------------------------
    Encipher a string using a shift cipher.
    Only letters are enciphered, and the returned string is
    in upper case.
    Use: estring = shift(string, n):
    -------------------------------------------------------
    Parameters:
        string - string to encipher (str)
        n - the number of letters to shift (int)
    Returns:
        estring - the enciphered string (str)
    -------------------------------------------------------
    """
    upper_string = string.upper()
    estring = ''
    i = 0
    j = 0
    while i < len(upper_string):
        if upper_string[i].isalpha():
            j = 0
            while upper_string[i] != ALPHABET[j]:
                j += 1
            num = j + n
            if num >= 26:
                num = num - ((num // 26) * 26)
            estring += ALPHABET[num]
        else:
            estring += upper_string[i]
        i += 1
    return estring
    
    
    
    
    
    
    
    
    