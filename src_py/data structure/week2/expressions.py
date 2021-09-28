from stack import Stack
from queue122 import Queue
from deque import Deque
import re
import doctest
import os

global OP_PREC
OP_PREC={"(":1,
         "+":2,
         "-":2,
         "*":3,
         "/":3,
         ")":4}



def calculate(operator, param1, param2):
    """
    Returns the result of a calculation between param1 and param2 using the
    given operator.
    Note: results may be floats...
    Supported operators: *, /, +, -, ^
    NOTE: We will use ^ to indicate ** for this exercise

    >>> calculate('*', 2, 3)
    6
    >>> calculate('+', 2, 3)
    5
    >>> calculate('-', 2, 3)
    -1
    """
    if operator == '*':
        return param1 * param2
    elif operator == '/':
        return param1 / param2
    elif operator == '+':
        return param1 + param2
    elif operator == '-':
        return param1 - param2
    elif operator == '^':
        return param1 ** param2
    else:
        raise Exception(operator+" is an invalid operator!")



def evaluate_postfix(expression):
    """
    Evaluates an expression in postfix notaion.
    Operands in the given expression must be integers.

    IMPORTANT NOTES:
    Make sure you operate on operands in the right order
    For example:  3 2 -   should be 3 - 2, not 2 - 3

    Intermediate values may be floats (eg, 3/4 gives 0.75)
    so don't cast anything to int after the input phase.

    >>> evaluate_postfix('2 3 +')
    5.0
    >>> evaluate_postfix('2 3 4 * +')
    14.0
    >>> evaluate_postfix('2 3 + 4 *')
    20.0
    >>> evaluate_postfix('2 3 2 * + 5 -')
    3.0
    >>> evaluate_postfix('2 3 + 2 5 - *')
    -15.0
    >>> evaluate_postfix('2 3 + 5 2 / *')
    12.5
    >>> evaluate_postfix('2 3 4 8 + * + 1 + 4 * 5 -')
    151.0
    """
    # Split postfix string into tokens. For example:
    #  '2 3 +' => ['2', '3', '+']
    # Don't worry about how this works
    tokens = re.findall(r'(\d+|\*|\+|\/|\-|\)|\(|\^)', expression)

    # NOTE: Intermediate values may be floats (eg, 3/4 gives 0.75)
    # so don't cast anything to int after the input phase.

    # Code to evaluate the postfix expression and return the result goes here
    # ---start student section---
    s = Stack()
    for token in tokens:
        if token.isdigit():
            s.push(token)
        else:
            param2 = s.pop()
            param1 = s.pop()
            s.push(calculate(token, float(param1), float(param2)))
            
    return s.pop()
            
    # ===end student section===


def infix_to_postfix(infix_expression):
    """
    Converts an infix expression to a postfix expression.
    Operands in the given expression must be integers.

    >>> infix_to_postfix('2 + 3')
    '2 3 +'
    >>> infix_to_postfix('2 + 3 * 4')
    '2 3 4 * +'
    >>> infix_to_postfix('(2 + 3) * 4')
    '2 3 + 4 *'
    >>> infix_to_postfix('2 + 3 * 2 - 5')
    '2 3 2 * + 5 -'
    >>> infix_to_postfix('(2 + 3) * (2 - 5)')
    '2 3 + 2 5 - *'
    >>> infix_to_postfix('(2 + 3) * (5 / 2)')
    '2 3 + 5 2 / *'
    >>> infix_to_postfix('2 + 3 * 4 / (6 - 4) + 1')
    '2 3 4 * 6 4 - / + 1 +'
    """

    # Split infix string into tokens. For example:
    #  '2+3*4' => ['2', '+', '3', '*', '4']
    # Operands must be integers.
    # Don't worry too much about how...
    tokens = re.findall(r'(\d+|\*|\+|\/|\-|\)|\(|\^)', infix_expression)

    #Code to process tokens and return the postfix string goes here
    # ---start student section---
    global OP_PREC
    result = []
    s = Stack()
    for token in tokens:
        if token == '(':
            s.push(token)
            
        elif token in '+-*/':
            if (not s.is_empty()) and (s.peek() in '+-*/'):
                while not s.is_empty() and OP_PREC[s.peek()] >= OP_PREC[token]:
                    result += [s.pop()]
            s.push(token)
                
            
        elif token == ')':
            symb = s.pop()
            while symb != '(':
                result += [symb]
                symb = s.pop()
            
        elif token.isdigit():
            result += [token]
            
    while not s.is_empty():
        result += [s.pop()]
    return ' '.join(result)
    # ===end student section===


def evaluate_infix(infix_expression):
    """
    Evaluates an infix expression.
    Operands in the given expression must be integers.

    >>> evaluate_infix('2 + 3 * 4')
    14.0
    >>> evaluate_infix('2 + (3 * 4)')
    14.0
    >>> evaluate_infix('(2 + 3) * 4')
    20.0
    >>> evaluate_infix('2 + 3 * 2 - 5')
    3.0
    >>> evaluate_infix('(2 + 3) * (2 - 5)')
    -15.0
    >>> evaluate_infix('(2 + 3) * (5 / 2)')
    12.5
    """

    # Split infix string into tokens. For example:
    #  '2+3*4' => ['2', '+', '3', '*', '4']
    # Operands must be integers
    # Don't worry too much about how...
    tokens = re.findall(r'(\d+|\*|\+|\/|\-|\)|\(|\^)', infix_expression)

    # Code to process tokens and evaluate the infix expression
    # See the Extras section of the handout.
    # As an extra exercise students can write code here that
    # evaluates infix directly (ie without converting to postfix first).
    # ---start student section---
    operator = Stack()
    operand = Stack()
    for token in tokens:
        if token.isdigit():
            operand.push(token)
            
        elif token in '+-*/':
            if (not operator.is_empty()) and (OP_PREC[operator.peek()] >= OP_PREC[token]):
                while (not operator.is_empty()) and (OP_PREC[operator.peek()] >= OP_PREC[token]):
                    op2 = operand.pop()
                    op1 = operand.pop()
                    operand.push(calculate(operator.pop(), float(op1), float(op2)))
            operator.push(token)
            
        elif token == '(':
            operator.push(token)
            
        elif token == ')':
            while operator.peek() != '(':
                op2 = operand.pop()
                op1 = operand.pop()
                operand.push(calculate(operator.pop(), float(op1), float(op2)))               
            operator.pop() 
        
    while not operator.is_empty():
        op2 = operand.pop()
        op1 = operand.pop()
        operand.push(calculate(operator.pop(), float(op1), float(op2)))
        
    return operand.pop()
            
    # ===end student section===




def evaluate_prefix(prefix_expression):
    """
    Evaluates a prefix expression directly, using a Deque.
    Operands must be integers and are initialy cast as ints.

    NOTE: Intermediate values may be floats (eg, 3/4 gives 0.75)
    so don't cast anything to int after the input phase.

    >>> evaluate_prefix('+ 2 4')
    6.0
    >>> evaluate_prefix('+ 2 * 4 3')
    14.0
    >>> evaluate_prefix('* + 2 * 1 2 8')
    32.0
    >>> evaluate_prefix('* - + 2 1 2 8')
    8.0
    >>> evaluate_prefix('+ / 8 - 6 2 4')
    6.0
    """

    # Split prefix string into tokens.
    tokens = re.findall(r'(\d+|\*|\+|\/|\-|\)|\(|\^)', prefix_expression)

    # add everything to a queue
    dq = Deque()
    for token in tokens:
        if token not in OP_PREC:
            # is a number so convert to a float
            token = float(token)
        dq.enqueue_rear(token)

    # etc
    # etc
    # etc
    # etc...
    # feel free to do this:)
    # and write some doctests to test that it works...




if __name__ == '__main__':
    #os.environ['TERM'] = 'linux' # Suppress ^[[?1034h

    # Uncomment the call to testmod to run the tests
    # Can enter an infinite loop if your Stack isn't implemented correctly
    # doctest.testmod()

    # Or you can test each thing separately
    doctest.run_docstring_examples(calculate, None)
    doctest.run_docstring_examples(evaluate_postfix, None)
    doctest.run_docstring_examples(infix_to_postfix, None)
    doctest.run_docstring_examples(evaluate_infix, None)
    # doctest.run_docstring_examples(evaluate_prefix, None)

