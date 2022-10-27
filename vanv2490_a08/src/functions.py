"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Levi Van Veen
ID: 200852490
Email: vanv2490@mylaurier.ca
__updated__ = "2021-03-25"
-------------------------------------------------------
"""
# Imports
from Letter import Letter

def do_comparisons(file_variable, bst):
    """
    -------------------------------------------------------
    Retrieves every letter in file_variable from bst. Generates
    comparisons in bst objects. Each Letter object in bst contains
    the number of comparisons found by searching for that Letter
    object in file_variable.
    Use: do_comparisons(file_variable, bst)
    -------------------------------------------------------
    Parameters:
        file_variable - the already open file containing data to evaluate (file)
        bst - the binary search tree containing 26 Letter objects
            to retrieve data from (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    # Zeroes out all comparison values in tree nodes
    for node in bst:
        node.comparisons = 0

    for v in file_variable:
        for letter in v:
            if letter.isalpha():
                var = Letter(letter.upper())
                bst.retrieve(var)
    
    return 

def comparison_total(bst):
    """
    -------------------------------------------------------
    Sums the comparison values of all Letter objects in bst.
    Use: total = comparison_total(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        total - the total of all comparison fields in the bst
            Letter objects (int)
    -------------------------------------------------------
    """
    total = 0
    a = bst.inorder()
    for v in a:
        total += v.comparisons
    return total


def letter_table(bst):
    """
    -------------------------------------------------------
    Prints a table of letter counts for each Letter object in bst.
    Use: letter_table(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    total = comparison_total(bst)
    
    print('Letter Count/Percent Table')
    print()
    print('Total Count: {:,}'.format(total))
    print()
    print('Letter  Count       %')
    print('---------------------')
    a = bst.inorder()
    for v in a:
        print('    {}  {}   {:.2f}%'.format(v.letter, v.comparisons, (v.comparisons / total) * 100))
    
    return

