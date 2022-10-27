"""
-------------------------------------------------------
Linked version of the Deque ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Term:    Winter 2020
__updated__ = "2021-04-08"
-------------------------------------------------------
"""
# Imports
from copy import deepcopy


class _Deque_Node:

    def __init__(self, value, _prev, _next):
        """
        -------------------------------------------------------
        Initializes a deque node.
        Use: node = _Deque_Node(value, _prev, _next)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            _prev - another deque node (_Deque_Node)
            _next - another deque node (_Deque_Node)
        Returns:
            a new _Deque_Node object (_Deque_Node)

        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._prev = _prev
        self._next = _next


class Deque:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty deque.
        Use: d = deque()
        -------------------------------------------------------
        Returns:
            a new Deque object (Deque)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the deque is empty.
        Use: b = deque.is_empty()
        -------------------------------------------------------
        Returns:
            True if the deque is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the deque.
        Use: n = len(deque)
        -------------------------------------------------------
        Returns:
            the number of values in the deque (int)
        -------------------------------------------------------
        """
        return self._count

    def insert_front(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the front of the deque.
        Use: deque.insert_front(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        node = _Deque_Node(value, None, None)
        if self._count == 0:
            self._front = node
            self._rear = self._front
        else:
            self._front._prev = node
            node._next = self._front
            self._front = node

        self._count += 1
        return

    def insert_rear(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the rear of the deque.
        Use: deque.insert_rear(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        node = _Deque_Node(value, None, None)
        if self._count == 0:
            self._front = node
            self._rear = self._front
        else:
            self._rear._next = node
            node._prev = self._rear
            self._rear = node
        self._count += 1
        return

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes and returns value from the front of the deque.
        Use: v = deque.remove_front()
        -------------------------------------------------------
        Returns:
            value - the value at the front of deque (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty deque"
        value = deepcopy(self._front._value)
        self._front = self._front._next
        if self._count > 1:
            self._front._prev = None
        else:
            self._front = None
            self._rear = None
        self._count -= 1
        return value

    def remove_rear(self):
        """
        -------------------------------------------------------
        Removes and returns value from the rear of the deque.
        Use: v = deque.remove_rear()
        -------------------------------------------------------
        Returns:
            value - the value at the rear of deque (?)
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot remove from an empty deque"
        value = deepcopy(self._rear._value)
        self._rear = self._rear._prev
        if self._count > 1:
            self._rear._next = None
        else:
            self._front = None
            self._rear = None
        self._count -= 1
        return value

    def peek_front(self):
        """
        -------------------------------------------------------
        Peeks at the front of deque.
        Use: v = deque.peek_front()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of deque (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty deque"
        value = deepcopy(self._front._value)
        return value

    def peek_rear(self):
        """
        -------------------------------------------------------
        Peeks at the rear of deque.
        Use: v = deque.peek_rear()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the rear of deque (?)
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot peek at an empty deque"
        value = deepcopy(self._rear._value)
        return value

    def _swap(self, l, r):
        """
        -------------------------------------------------------
        Swaps two nodes within a deque. l has taken the place of r, 
        r has taken the place of l and _front and _rear are updated 
        as appropriate. Data is not moved.
        Use: self._swap(self, l, r):
        -------------------------------------------------------
        Parameters:
            l - a pointer to a deque node (_Deque_Node)
            r - a pointer to a deque node (_Deque_Node)
        Returns:
            None
        -------------------------------------------------------
        """
        assert l is not None and r is not None, "nodes to swap cannot be None"
        if l._next == r:
            if self._front == l:
                self._front = r
                l._next = r._next
                r._prev = None
                l._prev = r
                r._next._prev = l
                r._next = l
            elif self._rear == r:
                self._rear = l
                l._prev._next = r
                r._next = l
                l._next = None
                r._prev = l._prev
                l._prev = r
            else:
                r._next._prev = l
                l._prev._next = r
                l._next = r._next
                r._next = l
                r._prev = l._prev
                l._prev = r

        elif r._next == l:
            if self._front == r:
                self._front = l
                r._next = l._next
                l._prev = None
                r._prev = l
                l._next._prev = r
                l._next = r
            elif self._rear == l:
                self._rear = r
                r._prev._next = l
                l._next = r
                r._next = None
                l._prev = r._prev
                r._prev = l
            else:
                l._next._prev = r
                r._prev._next = l
                r._next = l._next
                l._next = r
                l._prev = r._prev
                r._prev = l

        elif l._prev is not None and l._next is not None:
            # Both are not front or rear
            if r._prev is not None and r._next is not None:
                # Make nodes around the nodes point at swapped nodes
                l._prev._next = r
                r._prev._next = l
                l._next._prev = r
                r._next._prev = l

                # swap pointers on nodes themselves
                temp = r._next
                r._next = l._next
                l._next = temp
                temp = r._prev
                r._prev = l._prev
                l._prev = temp

            # l is not front or rear, r is the rear
            elif r._prev is not None:
                # Making nodes around l and r point at swapped nodes
                l._prev._next = r
                r._prev._next = l
                l._next._prev = r

                # Swap pointers on nodes themselves
                r._next = l._next
                l._next = None
                temp = r._prev
                r._prev = l._prev
                l._prev = temp

                self._rear = l

            # l is not front or rear, r is the front
            else:
                # Making nodes around l and r point at swapped nodes
                l._prev._next = r
                l._next._prev = r
                r._next._prev = l

                # Swap pointers on nodes themselves
                r._prev = l._prev
                l._prev = None
                temp = r._next
                r._next = l._next
                l._next = temp

                self._front = l

        # l is the rear
        elif l._prev is not None:
            # L is the rear, r is not the rear or front
            if r._prev is not None and r._next is not None:
                # Make nodes around l and r point at swapped nodes
                l._prev._next = r
                r._prev._next = l
                r._next._prev = l

                # swap pointers on nodes themselves
                l._next = r._next
                r._next = None
                temp = l._prev
                l._prev = r._prev
                r._prev = temp

                self._rear = r

            # l is the rear, r is the front
            elif r._next is not None:
                # Make nodes around l and r point at swapped nodes
                l._prev._next = r
                r._next._prev = l

                # swap pointers on nodes themselves
                r._prev = l._prev
                l._prev = None
                l._next = r._next
                r._next = None

                self._front = l
                self._rear = r
        # L is the front
        elif l._next is not None:
            # l is the front and r is not rear
            if r._prev is not None and r._next is not None:
                # Make nodes around point at l and r
                l._next._prev = r
                r._next._prev = l
                r._prev._next = l

                # swap pointers
                l._prev = r._prev
                r._prev = None
                temp = l._next
                l._next = r._next
                r._next = temp

                self._front = r
            #L is front and r is rear
            elif r._prev is not None:
                # Make nodes around l and r point at swapped nodes
                r._prev._next = l
                l._next._prev = r

                # swap pointers on nodes themselves
                l._prev = r._prev
                r._prev = None
                r._next = l._next
                l._next = None

                self._front = r
                self._rear = l
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the deque
        from front to rear.
        Use: for v in d:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the deque (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next
