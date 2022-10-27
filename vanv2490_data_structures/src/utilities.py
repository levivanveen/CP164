"""
-------------------------------------------------------
[utilities]
-------------------------------------------------------
Author: Levi Van Veen
ID: 200852490
Email: vanv2490@mylaurier.ca
__updated__ = "2021-01-27"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from Movie import Movie
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue
from List_array import List
from copy import deepcopy
# Constants

def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    i = 0
    length = len(source)
    while i < length:
        stack.push(source[length - 1 - i])
        source.pop(length - 1 - i)
        i += 1
    return 


def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not stack.is_empty():
        target.insert(0,stack.pop())
    
    return


def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    stack = Stack()
    if stack.is_empty():
        print("The stack is empty")
        print()
        for v in source:
            stack.push(v)
            print("{}".format(v))
            print("was pushed to the stack")
            print()
    else:
        print("The stack is not empty")
        print()
        for v in source:
            stack.push(v)
            print("{}".format(v))
            print("was pushed to the stack")
            print()
    
    if stack.is_empty():
        print("The stack is still empty")
    else:
        print("The stack is not empty")
    print()
    print("The top of the stack is {}".format(stack.peek()))
    print()
    print("The last item removed from the stack is {}".format(stack.pop()))
    return 


def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    i = 0
    length = len(source)
    while i < length:
        queue.insert(source[0])
        source.pop(0)
        i += 1
    return


def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    i = 0
    length = len(queue)
    while i < length:
        target.append(queue.remove())
        i += 1
    
    return


def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    i = 0
    length = len(source)
    while i < length:
        pq.insert(source[0])
        source.pop(0)
        i += 1
    return


def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    i = 0
    length = len(pq)
    while i < length:
        target.append(pq.remove())
        i += 1
    
    return
    
def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
    Tests the methods of Queue are tested for both empty and
    non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    q = Queue()
    if q.is_empty():
        print("The queue is empty")
        print()
    else:
        print("The queue is not empty")
        print()
    for v in a:
        q.insert(v)
    print('The first item in the queue is {}'.format(q.peek()))
    print()
    print('The item that was just removed from the queue is {}'.format(q.remove()))
    print()
    print('The first item in the queue is now {}'.format(q.peek()))
    # tests for the queue methods go here
    # print the results of the method calls and verify by hand

    return


def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: priority_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()
    
    if pq.is_empty():
        print("The queue is empty")
        print()
    else:
        print("The queue is not empty")
        print()
    for v in a:
        pq.insert(v)
    print('The first item in the queue is {}'.format(pq.peek()))
    print()
    print('The item that was just removed from the queue is {}'.format(pq.remove()))
    print()
    print('The first item in the queue is now {}'.format(pq.peek()))

    return


def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist,
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) > 0:
        llist.append(source.pop(0))
    
    return

def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(llist) > 0:
        target.append(llist.pop(0))
    return

def list_test(source):
    """
    -------------------------------------------------------
    Tests List implementation.
    The methods of List are tested for both empty and
    non-empty lists using the data in source
    Use: list_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()
    if lst.is_empty():
        print('The list is empty')
    for v in source:
        lst.append(deepcopy(v))
        print('an item was added to the list')
        print()
        
    for v in source:
        if len(lst) > 9:
            lst.insert(10,deepcopy(v))
            print('{} was added to the list'.format(v))
            print()
            
    if not lst.is_empty():
        print('The list is not empty')
        
    print()
    print('The first item in the list is {}'.format(lst.peek()))
    print()
    print('The largest item in the list is {}'.format(lst.max()))
    print()
    print('The item that was removed is {}'.format(lst.remove(lst.max())))
    print()
    print("The smallest item in the list is {}\nand it's index is {}.\nIt is in the list {} time(s).".format(lst.find(lst.min()),lst.index(lst.min()),lst.count(lst.min())))
    print()
    # tests for the List methods go here
    # print the results of the method calls and verify by hand

    return


