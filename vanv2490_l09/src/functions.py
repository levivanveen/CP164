"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Levi Van Veen
ID: 200852490
Email: vanv2490@mylaurier.ca
__updated__ = "2021-03-24"
-------------------------------------------------------
"""
# Imports

def hash_table(slots, values):
    """
    -------------------------------------------------------
    Print a hash table of a set of values. The format is:
    Hash     Slot Key
    --------------------------------
    1652346    3 Dark City, 1998
    848448    6 Zulu, 1964
    Do not create an actual Hash_Set.
    Use: hash_table(slots, values)
    -------------------------------------------------------
    Parameters:
       slots - the number of slots available (int > 0)
       values - the values to hash (list of ?)
    Returns:
       None
    -------------------------------------------------------
    """
    print('Hashes')
    print('Hash     Slot Key')
    print('-------- ---- --------------------')
    
    for v in values:
        h = hash(v)
        print(' {:>8} {:>4} {}, {}'.format(h, h % slots, v.title, v.year))
    return