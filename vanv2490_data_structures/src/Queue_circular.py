"""
-------------------------------------------------------
Circular array version of the Queue ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Term:    CP164B - Winter 2021
__updated__ = "2021-01-12"
-------------------------------------------------------
"""
# pylint: disable=protected-access

from copy import deepcopy


class Queue:
    """
    -------------------------------------------------------
    Constants
    -------------------------------------------------------
    """
    # a default maximum size when one is not provided
    DEFAULT_SIZE = 10

    def __init__(self, max_size=DEFAULT_SIZE):
        """
        -------------------------------------------------------
        Initializes an empty queue. Data is stored in a fixed-size list.
        Use: target = Queue(max_size)
        Use: target = Queue()  # uses default max size
        -------------------------------------------------------
        Parameters:
            max_size - maximum size of the queue (int > 0)
        Returns:
            a new Queue object (Queue)
        -------------------------------------------------------
        """
        assert max_size > 0, "Queue size must be > 0"

        self._max_size = max_size
        self._values = [None] * self._max_size
        self._front = None
        self._rear = 0
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the queue is empty.
        Use: empty = source.is_empty()
        -------------------------------------------------------
        Returns:
            True if the queue is empty, False otherwise.
        -------------------------------------------------------
        """
        empty = True
        for v in self._values:
            if v != None:
                empty = False
        return empty

    def is_full(self):
        """
        -------------------------------------------------------
        Determines if the queue is full.
        Use: full = source.is_full()
        -------------------------------------------------------
        Returns:
            True if the queue is full, False otherwise.
        -------------------------------------------------------
        """
        full = True
        for v in self._values:
            if v == None:
                full = False
        return full
    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the queue.
        Use: n = len(source)
        -------------------------------------------------------
        Returns:
            the number of values in the queue.
        -------------------------------------------------------
        """
        length = 0
        for v in self._values:
            if v != None:
                length += 1
        return length
        
    def insert(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the rear of the queue.
        Use: source.insert( value )
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot add to a full queue"
        
        self._values[self._rear] = deepcopy(value)
        
        if self._front == None:
            self._front = self._rear
        self._rear += 1
        
        if self._rear == self._max_size and self.is_full() == False:
            self._rear = 0
        elif self.is_full() == True:
            self._rear = None
        self._count += 1

        return
    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns value from the queue.
        Use: v = source.remove()
        -------------------------------------------------------
        Returns:
            value - the value at the front of the queue - the value is
                removed from the queue (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty queue"
        
        value = deepcopy(self._values[self._front])
        self._values[self._front] = None
        if self._rear == None:
            self._rear = self._front
        if self._front == self._max_size - 1:
            self._front = 0
        else:
            self._front += 1
            
        if self.is_empty() == True:
            self._front = None

        self._count -= 1
        return value
    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the front of queue.
        Use: v = source.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of the queue -
                the value is not removed from the queue (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot peek at an empty queue"
        value = deepcopy(self._values[self._front])
        return value

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for v in cq:
        -------------------------------------------------------
        Returns:
            value - the next value in the queue (?)
        -------------------------------------------------------
        """
        value = self._values[self._front]
        if self._front is not None:
            # queue is not empty
            j = self._front
            i = 0

            while i < self._count:
                yield self._values[j]
                i += 1
                j = (j + 1) % self._max_size
        return value
    
    
    def is_identical(self, target):
        """
        ----------------
        Determines whether two queues are identical.
        Entries of self and target are compared and if all contents are identical
        and in the same order, returns True, otherwise returns False.
        Use: identical = source.is_identical(target)
        ---------------
        Parameters:
            target - a queue (Queue)
        Returns:
            identical - True if self and target are identical, False otherwise.
                source and target are unchanged. (boolean)
        ---------------
        """
        identical = True
        i = 0
        if self.__len__() != target.__len__():
            identical = False
        while i < self.__len__() and identical == True:
            if self._values[i] != target._values[i]:
                identical = False
            i += 1
        
        return identical
    
    
    