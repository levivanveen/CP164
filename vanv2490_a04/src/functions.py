"""
-------------------------------------------------------
Assignment 4 Functions
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2021-02-23"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue
from utilities import array_to_queue


def queue_is_identical(source1, source2):
    """
    ----------------
    Determines whether two given queues are identical. Entries of
    source1 and source2 are compared and if all contents are identical
    and in the same order, returns True, otherwise returns False.
    Use: identical = queue_is_identical(source1, source2)
    ---------------
    Parameters:
        source1 - a queue (Queue)
        source2 - a queue (Queue)
    Returns:
        identical - True if source1 and source2 are identical, False otherwise.
            source1 and source2 are unchanged. (boolean)
    ---------------
    """
    identical = True

    if len(source1) != len(source2):
        identical = False
    else:
        # Queues must be of same length
        t1 = []
        t2 = []

        while identical and not source1.is_empty():
            # Remove and test queues' individual values
            v1 = source1.remove()
            v2 = source2.remove()

            if v1 != v2:
                # Values do not match.
                identical = False
            t1.append(v1)
            t2.append(v2)

        while not source1.is_empty():
            # Clean up queues
            t1.append(source1.remove())
            t2.append(source2.remove())

        # Copy the data back to the queues.
        array_to_queue(source1, t1)
        array_to_queue(source2, t2)
    return identical


def pq_split_key(source, key):
    """
    -------------------------------------------------------
    Splits a priority queue into two depending on an external
    priority key. The source priority queue is empty when the method
    ends. The order of the values from source is preserved.
    Use: target1, target2 = pq_split_key(source, key)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
        key - a data object (?)
    Returns:
        target1 - a priority queue that contains all values
            with priority higher than key (Priority_Queue)
        target2 - priority queue that contains all values with
            priority lower than or equal to key (Priority_Queue)
    -------------------------------------------------------
    """
    target1 = Priority_Queue()
    target2 = Priority_Queue()

    while not source.is_empty():
        v = source.remove()

        if v < key:
            target1.insert(v)
        else:
            target2.insert(v)
    return target1, target2
