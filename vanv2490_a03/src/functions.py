"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Levi Van Veen
ID: 200852490
Email: vanv2490@mylaurier.ca
__updated__ = "2021-02-04"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from enum import Enum

# Constants
OPERATORS = "+-*/"
# Enumerated constant
MIRRORED = Enum('MIRRORED',
                {'IS_MIRRORED': "is a mirror", 'TOO_MANY_LEFT': "too many characters in L",
                 'TOO_MANY_RIGHT': "too many characters in R", 'MISMATCHED': "L and R don't match",
                 'INVALID_CHAR': "invalid character", 'NOT_MIRRORED': "no mirror character"})

def stack_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source stack into separate target stacks.
    When finished source stack is empty. Values are
    pushed alternately onto the returned target stacks.
    Use: target1, target2 = stack_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - the stack to split into two parts (Stack)
    Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
    -------------------------------------------------------
    """
    i = 0
    target1 = Stack()
    target2 = Stack()
    while source.is_empty() == False:
        if (i % 2) == 0:
            value = source.pop()
            target1.push(value)
        else:
            value = source.pop()
            target2.push(value)
        i += 1
    return target1, target2


def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    i = 0
    list = []
    while source.is_empty() == False:
        list.append(source.pop())
    length = len(list)
    while i < length:
        source.push(list[0])
        list.pop(0)
        i += 1
    return


def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    s = Stack()
    i = 0
    while i < len(string):
        ch = string[i]
        if ch != ' ':
            if ch.isnumeric():
                if i + 1 >= len(string):
                    s.push(int(ch))
                else:
                    check = string[(i + 1)]
                    while check != ' ':
                        ch += string[(i + 1)]
                        i += 1
                        if i + 1 >= len(string):
                            check = ' '
                        else:
                            check = string[(i + 1)]
                    s.push(int(ch))
            elif ch in OPERATORS:
                first = s.pop()
                second = s.pop()
                if ch == '+':
                    value = second + first
                    s.push(value)
                    
                elif ch == '-':
                    value = second - first
                    s.push(value)
                    
                elif ch == '*':
                    value = second * first
                    s.push(value)
                    
                elif ch == '/':
                    value = second / first
                    s.push(value)
        i += 1
    answer = s.pop()
    return answer        
            
            
def reroute(opstring, values_in):
    """
    -------------------------------------------------------
    Reroutes values in a list according to a operating string and
    returns a new list of values. values_in is unchanged.
    In opstring, 'S' means push onto stack,
    'X' means pop from stack into values_out.
    Use: values_out = reroute(opstring, values_in)
    -------------------------------------------------------
    Parameters:
        opstring - String containing only 'S' and 'X's (str)
        values_in - A valid list (list of ?)
    Returns:
        values_out - if opstring is valid then values_out contains a
            reordered version of values_in, otherwise returns
            None (list of ?)
    -------------------------------------------------------
    """
    values_out = []
    s = Stack()
    i = 0
    j = 0
    if len(opstring) != len(values_in) * 2:
        values_out = None
    while i < len(opstring) and values_out != None:
        ch = opstring[i]
        if ch == 'S':
            s.push(values_in[j])
            j += 1
        elif ch == 'X':
            if s.is_empty() == True and i != (len(opstring) - 1):
                values_out = None
            else:
                values_out.append(s.pop())
        i += 1
    return values_out
    
    
    
def is_mirror_stack(string, valid_chars, m):
    """
    -------------------------------------------------------
    Determines if string is a mirror of characters in valid_chars around the pivot m.
    A mirror is of the form LmR, where L is the reverse of R, and L and R
    contain only characters in valid_chars.
    Use: mirror = is_mirror_stack(string, valid_chars, m)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
        valid_chars - a string of valid characters (str)
        m - the mirror pivot string (str - one character not in valid_chars)
    Returns:
        mirror - the state of the string (Enum MIRRORED)
    -------------------------------------------------------
    """
    assert m not in valid_chars, \
        "cannot use '{}' as the mirror character".format(m)
        
    mirror = ''
    s = Stack()
    i = 0
    if m in string:
        while i < len(string) and string[i] != m:
            ch = string[i]
            if ch not in valid_chars:
                mirror = MIRRORED.INVALID_CHAR
            else:
                s.push(ch)
            i += 1
        
        #Check If sides are equal length
        left_length = i
        i += 1
        length_mid = left_length + 1
        right_length = len(string) - length_mid
        if right_length > left_length:
            mirror = MIRRORED.TOO_MANY_RIGHT
        elif right_length < left_length:
            mirror = MIRRORED.TOO_MANY_LEFT
        
        #Check if right side equals left, and if right side has all correct characters
        while i < len(string) and not s.is_empty() and mirror == '':
            ch = string[i]
            letter = s.pop()
            if ch not in valid_chars:
                mirror = MIRRORED.INVALID_CHAR
            else:  
                if ch != letter:
                    mirror = MIRRORED.MISMATCHED
            i += 1
            
        
    else:
        mirror = MIRRORED.NOT_MIRRORED
        
        
    if mirror == '':
        mirror = MIRRORED.IS_MIRRORED
    return mirror
    
    
    
    
    
        
        
        
        
        