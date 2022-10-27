"""
-------------------------------------------------------
Array version of the Stack ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Term:    Winter 2020
__updated__ = "2020-01-16"
-------------------------------------------------------
"""
from copy import deepcopy


class Stack:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty stack. Data is stored in a Python list.
        Use: stack = Stack()
        -------------------------------------------------------
        Returns:
            a new Stack object (Stack)
        -------------------------------------------------------
        """
        self._values = []

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source stacks into the current target stack. 
        When finished, the contents of source1 and source2 are 
        interlaced into target and source1 and source2 are empty.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based stack (Stack)
            source2 - an array-based stack (Stack)
        Returns:
            None
        -------------------------------------------------------
        """
        i = 0
        while source1.is_empty() == False:
            if source2.is_empty() == False:
                if i % 2 == 0:
                    self._values.append(deepcopy(source1._values.pop()))
                elif i % 2 != 0:
                    self._values.append(deepcopy(source2._values.pop()))
                    
            else:
                self._values.append(source1._values.pop())
            i += 1
        while source2.is_empty() == False:
            self._values.append(deepcopy(source2._values.pop()))         

        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the stack is empty.
        Use: b = stack.is_empty()
        -------------------------------------------------------
        Returns:
            True if stack is empty, False otherwise
        -------------------------------------------------------
        """
        empty = True
        
        if len(self._values) > 0:
            empty = False
            
        return empty

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the value at the top of the stack.
        Attempting to peek at an empty stack throws an exception.
        Use: value = stack.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the top of stack (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot peek at an empty stack'

        value = deepcopy(self._values[len(self._values) - 1])

        return value

    def pop(self):
        """
        -------------------------------------------------------
        Pops and returns the top of stack. The value is removed
        from the stack. Attempting to pop from an empty stack
        throws an exception.
        Use: value = stack.pop()
        -------------------------------------------------------
        Returns:
            value - the value at the top of stack (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot pop from an empty stack'

        value = deepcopy(self._values.pop())

        return value

    def push(self, value):
        """
        -------------------------------------------------------
        Pushes a copy of value onto the top of the stack.
        Use: stack.push(value)
        -------------------------------------------------------
        Parameters:
            value - value to be added to stack (?)
        Returns:
            None
        -------------------------------------------------------
        """
        self._values.append(deepcopy(value))
        
        return

    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the contents of the source stack.
        Use: stack.reverse()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        list = []
        i = 0
        length = len(self._values)
        while i < length:
            list.append(deepcopy(self._values.pop()))
            i += 1
        for v in list:
            self._values.append(deepcopy(v))
        return

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source stack into separate target stacks with values 
        alternating into the targets. At finish source stack is empty.
        (iterative algorithm)
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (Stack)
            target2 - contains other alternating values from source (Stack)
        -------------------------------------------------------
        """
        target1 = Stack()
        target2 = Stack()
        
        i = 0
        length = len(self._values)
        while i < length:
            if i % 2 == 0:
                target1.push(deepcopy(self._values.pop()))
            else:
                target2.push(deepcopy(self._values.pop()))
            i += 1

        return target1, target2

    def __iter__(self):
        """
        FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the stack
        from top to bottom.
        Use: for value in stack:
        -------------------------------------------------------
        Returns:
            value - the next value in the stack (?)
        -------------------------------------------------------
        """
        for value in self._values[::-1]:
            yield value

