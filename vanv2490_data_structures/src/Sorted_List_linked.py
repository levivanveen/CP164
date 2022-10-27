"""
-------------------------------------------------------
Linked version of the Sorted_List ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Term:    Winter 2020
__updated__ = "2021-04-19"
-------------------------------------------------------
"""
# Imports
from copy import deepcopy


class _SL_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a sorted list node.
        Use: node = _SL_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            next_ - another sorted list node (_SL_Node)
        Returns:
            Initializes a list node that contains a copy of value
            and a link to the next node in the list.
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_
        return


class Sorted_List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty Sorted_List.
        Use: sl = Sorted_List()
        -------------------------------------------------------
        Returns:
            a Sorted_List object (Sorted_List)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = sl.is_empty()
        -------------------------------------------------------
        Returns:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the list.
        Use: n = len(l)
        -------------------------------------------------------
        Returns:
            Returns the number of values in the list.
        -------------------------------------------------------
        """
        length = self._count
        return length

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts value at the proper place in the sorted list.
        Must be a stable insertion, i.e. consecutive insertions
        of the same value must keep their order preserved.
        Use: sl.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            value inserted at its sorted position within the sorted list.
        -------------------------------------------------------
        """
        inserted = False
        node = _SL_Node(value, None)
        if self._count > 0:
            if value < self._front._value:
                node._next = self._front
                self._front = node
                inserted = True
            current = self._front
            previous = None
            while current is not None and not inserted:
                if node._value < current._value:
                    previous._next = node
                    node._next = current
                    inserted = True
                else:
                    previous = current
                    current = current._next
            if not inserted:
                self._rear._next = node
                self._rear = node
        else:
            self._front = node
            self._rear = self._front
        self._count += 1
        return

    def _linear_search(self, key):
        """
        Cannot do a (simple) binary search on a linked structure. 
        -------------------------------------------------------
        Searches for the first occurrence of key in the sorted list. 
        Performs a stable search.
        Private helper method - used only by other ADT methods.
        Use: i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_SL_Node)
            current - pointer to the node containing key (_SL_Node)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """
        found = False
        current = self._front
        index = 0
        previous = None

        while current is not None and not found:
            if key == current._value:
                found = True
            else:
                previous = current
                current = current._next
                index += 1
        if found == False:
            current = None
            index = -1
        return previous, current, index

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in the sorted list that matches key.
        Use: value = sl.remove( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        previous, current, index = self._linear_search(key)
        if index != -1:
            value = current._value
            self._count -= 1
            if current == self._front:
                self._front = current._next
            elif current == self._rear:
                previous._next = None
                self._rear = previous
            else:
                previous._next = current._next
            if self._count == 0:
                self._rear = None
                self._front = None
        else:
            value = None

        return value

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first node in the list and returns its value.
        Use: value = lst.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty list"
        value = self._front._value
        if self._count > 1:
            self._front = self._front._next
        else:
            self._front = None
            self._rear = None
        self._count -= 1

        return value

    def remove_many(self, key):
        """
        -------------------------------------------------------
        Finds and removes all values in the list that match key.
        Use: l.remove_many(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            All values matching key are removed from the list.
        -------------------------------------------------------
        """
        previous, current, index = self._linear_search(key)
        if index != -1:
            while current is not None and current._value == key:
                if current == self._front:
                    self._front = current._next
                elif current == self._rear:
                    previous._next = None
                    self._rear = previous
                else:
                    previous._next = current._next
                self._count -= 1
                current = current._next
            if self._count == 0:
                self._rear = None
                self._front = None
        return

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in list that matches key.
        Use: value = l.find( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        value = None
        if self._front is not None:
            _, current, index = self._linear_search(key)
            if index != -1:
                value = current._value
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = l.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty list"
        value = deepcopy(self._front._value)
        return value

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = l.index( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of the location of key in the list, -1 if
              key is not in the list.
        -------------------------------------------------------
        """
        _, _, i = self._linear_search(key)
        if i == None:
            i = -1
        return i

    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(list) to len(list) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        n = self._count
        return -n <= i < n

    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of the list.
        Use: value = l[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of list (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"

        current = self._front
        if i < 0:
            i = self._count + i
        while i > 0:
            current = current._next
            i -= 1
        value = deepcopy(current._value)
        return value

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the list contains key.
        Use: b = key in l
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if the list contains key, False otherwise.
        -------------------------------------------------------
        """
        _, _, index = self._linear_search(key)
        return index != -1

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in the sorted list.
        Use: value = sl.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the sorted list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"
        value = deepcopy(self._rear._value)
        return value

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in the sorted list.
        Use: value = sl.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the sorted list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find minimum of an empty list"
        value = deepcopy(self._front._value)
        return value

    def count(self, key):
        """
        -------------------------------------------------------
        Determines the number of times key appears in the sorted list.
        Use: n = sl.count(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            number - the number of times key appears in the sorted list (int)
        -------------------------------------------------------
        """
        number = 0
        previous, current, index = self._linear_search(key)
        if index != -1:
            while current is not None and current._value == key:
                number += 1
                current = current._next
        return number

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the sorted list. The list contains 
        one and only one of each value formerly present in the list. 
        The first occurrence of each value is preserved.
        Use: source.clean()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        if self._count > 1:
            current = self._front._next
            previous = self._front
            while current is not None:
                if current is not None and previous._value == current._value:
                    if current == self._rear:
                        previous._next = None
                        self._rear = previous._next
                    else:
                        previous._next = current._next
                    self._count -= 1
                else:
                    previous = previous._next
                current = current._next
        return

    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list whose index matches i.
        Use: value = lst.pop()
        Use: value = lst.pop(i)
        -------------------------------------------------------
        Parameters:
            args - an array of arguments (tuple of int)
            args[0], if it exists, is the index i
        Returns:
            value - if args exists, the value at position args[0], 
                otherwise the last value in the list, value is 
                removed from the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"

        previous = None
        current = self._front

        if len(args) == 1:
            i = args[0]

            if i < 0:
                # index is negative
                i = self._count + i
            j = 0

            while j < i:
                previous = current
                current = current._next
                j += 1
        else:
            # find and pop the last element
            j = 0

            while j < (self._count - 1):
                previous = current
                current = current._next
                j += 1

        value = current._value

        if previous is None:
            # Update the front
            self._front = current._next
        else:
            # Update any other node
            previous._next = current._next
        self._count -= 1
        return value

    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (iterative algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        source1_current = source1._front

        while source1_current is not None:
            value = source1_current._value
            if value in source2:
                _, _, index, = self._linear_search(value)
                if index == -1:
                    inserted = False
                    node = _SL_Node(value, None)
                    if self._count > 0:
                        if value < self._front._value:
                            node._next = self._front
                            self._front = node
                            inserted = True
                        current = self._front
                        previous = None
                        while current is not None and not inserted:
                            if node._value < current._value:
                                previous._next = node
                                node._next = current
                                inserted = True
                            else:
                                previous = current
                                current = current._next
                        if not inserted:
                            self._rear._next = node
                            self._rear = node
                    else:
                        self._front = node
                        self._rear = self._front
                    self._count += 1
            source1_current = source1_current._next

        return

    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (iterative algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked list (List)
            source2 - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        source1 = source1._front
        source2 = source2._front

        while source1 is not None:
            _, _, index, = self._linear_search(source1._value)
            value = source1._value
            if index == -1:
                inserted = False
                node = _SL_Node(value, None)
                if self._count > 0:
                    if value < self._front._value:
                        node._next = self._front
                        self._front = node
                        inserted = True
                    current = self._front
                    previous = None
                    while current is not None and not inserted:
                        if node._value < current._value:
                            previous._next = node
                            node._next = current
                            inserted = True
                        else:
                            previous = current
                            current = current._next
                    if not inserted:
                        self._rear._next = node
                        self._rear = node
                else:
                    self._front = node
                    self._rear = self._front
                self._count += 1
            source1 = source1._next

        while source2 is not None:
            _, _, index, = self._linear_search(source2._value)
            value = source2._value
            if index == -1:
                inserted = False
                node = _SL_Node(value, None)
                if self._count > 0:
                    if value < self._front._value:
                        node._next = self._front
                        self._front = node
                        inserted = True
                    current = self._front
                    previous = None
                    while current is not None and not inserted:
                        if node._value < current._value:
                            previous._next = node
                            node._next = current
                            inserted = True
                        else:
                            previous = current
                            current = current._next
                    if not inserted:
                        self._rear._next = node
                        self._rear = node
                else:
                    self._front = node
                    self._rear = self._front
                self._count += 1

            source2 = source2._next

        return

    def split_th(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. At finish self is empty.
        Uses Tortoise/Hare algorithm.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """

        # your code here

        return

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits list so that target1 contains all values <= key,
        and target2 contains all values > key. At finish self is empty.
        Use: target1, target2 = lst.split_key()
        -------------------------------------------------------
        Returns:
            target1 - a new List of values <= key (List)
            target2 - a new List of values > key (List)
        -------------------------------------------------------
        """

        # your code here

        return

    def split_alt(self):
        """
        -------------------------------------------------------
        Split a List into two parts. even contains the even indexed
        elements, odd contains the odd indexed elements. At finish
        self is empty. Order of even and odd is not significant.
        (iterative version)
        Use: even, odd = l.split_alt()
        -------------------------------------------------------
        Returns:
            even - the even indexed elements of the list (Sorted_List)
            odd - the odd indexed elements of the list (Sorted_List)
                The List is empty.
        -------------------------------------------------------
        """

        # your code here

        return

    def split(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. At finish self is empty.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """

        # your code here

        return

    def is_identical(self, other):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical. (iterative version)
        Use: b = l.is_identical(other)
        -------------------------------------------------------
        Parameters:
            other - another list (Sorted_List)
        Returns:
            identical - True if this list contains the same values as
                other in the same order, otherwise False.
        -------------------------------------------------------
        """
        if self._count != other._count:
            identical = False
        else:
            source_node = self._front
            target_node = other._front

            while source_node is not None and source_node._value == target_node._value:
                source_node = source_node._next
                target_node = target_node._next

            identical = source_node is None
        return identical

    def copy(self):
        """
        -------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (iterative version)
        Use: new_list = l.copy()
        -------------------------------------------------------
        Returns:
            new_list - a copy of self (Sorted_List)
        -------------------------------------------------------
        """
        new_list = Sorted_List()

        current = self._front
        if current is not None:
            node = _SL_Node(deepcopy(current._value), None)
            new_list._front = node
            current = current._next
            new_list._count += 1
        new_current = new_list._front
        while current is not None:
            node = _SL_Node(deepcopy(current._value), None)
            new_current._next = node
            new_current = node
            current = current._next
            new_list._count += 1
        new_list._rear = new_current

        return new_list

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        At finish, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked list (List)
            source2 - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        current = source1._front
        other = source2._front
        while current is not None and other is not None:
            if current._value < other._value:
                next_one = current._next
                if len(self) == 0:
                    self._front = current
                    self._rear = current
                    current._next = None
                else:
                    self._rear._next = current
                    self._rear = current
                    self._rear._next = None
                current = next_one
            else:
                next_one = other._next
                if len(self) == 0:
                    self._front = other
                    self._rear = other
                    other._next = None
                else:
                    self._rear._next = other
                    self._rear = other
                    self._rear._next = None
                other = next_one
            self._count += 1

        if other is None:
            while current is not None:
                next_one = current._next
                if len(self) == 0:
                    self._front = current
                    self._rear = current
                    self._rear._next = None
                else:
                    self._rear._next = current
                    self._rear = current
                    self._rear._next = None
                current = next_one
                self._count += 1
        else:
            while other is not None:
                next_one = other._next
                if len(self) == 0:
                    next_one = other._next
                    self._front = other
                    self._rear = other
                    self._rear._next = None
                else:
                    self._rear._next = other
                    self._rear = other
                    self._rear._next = None
                self._count += 1
                other = next_one
        source1._front = None
        source2._front = None
        source1._rear = None
        source2._rear = None
        source1._count = 0
        source2._count = 0
        return

    def _linear_search_r(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the list.
        Private helper methods - used only by other ADT methods.
        (recursive version)
        Use: p, c, i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_SL_Node)
            current - pointer to the node containing key (_SL_Node)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """

        # your code here

        return

    def clean_r(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the sorted list.
        Use: sl.clean_r()
        -------------------------------------------------------
        Returns:
            The list contains one and only one of each value formerly present
            in the list. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """

        # your code here

        return

    def identical_r(self, rs):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical. (recursive version)
        Use: b = l.identical_r(rs)
        -------------------------------------------------------
        Parameters:
            rs - another list (Sorted_List)
        Returns:
            identical - True if this list contains the same values as rs
                in the same order, otherwise False.
        -------------------------------------------------------
        """

        # your code here

        return

    def intersection_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        (recursive algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """

        return

    def copy_r(self):
        """
        -----------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (recursive verstion)
        Use: new_list = l.copy()
        -----------------------------------------------------------
        Returns:
            new_list - a copy of self (Sorted_List)
        -----------------------------------------------------------
        """
        new_list = Sorted_List()
        old_current = self._front

        self._copy_r_aux(old_current, new_list, None)

        return new_list

    def _copy_r_aux(self, old_current, new_list, node):

        temp = node
        if old_current is not None:
            node = _SL_Node(old_current._value, None)
            if old_current is self._front:
                new_list._front = node
            else:
                temp._next = node
            self._copy_r_aux(old_current._next, new_list, node)
        else:
            new_list._rear = node

        return

    def combine_r(self, rs):
        """
        -------------------------------------------------------
        Combines contents of two lists into a third.
        Use: new_list = l1.combine(rs)
        -------------------------------------------------------
        Parameters:
            rs- an linked-based List (Sorted_List)
        Returns:
            new_list - the contents of the current Sorted_List and rs
            are interlaced into new_list - current Sorted_List and rs
            are empty (Sorted_List)
        -------------------------------------------------------
        """

        # your code here

        return

    def union_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat.
        (recursive algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked list (List)
            source2 - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """

        # your code here

        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next
