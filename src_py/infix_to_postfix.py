import string
from abstract_data_type import Stack
import doctest

def infixToPostfix(infixexpr):
    """>>> infixexpr1 = 'A + ( ( B + C ) * ( D + E ) )'
       >>> print(infixToPostfix(infixexpr1))
       ABC+DE+*+
       >>> infixexpr1 = '( A + B ) * ( C + D ) * ( E + F )'
       >>> print(infixToPostfix(infixexpr1))
       AB+CD+*EF+*
    """

    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    
    load_Stack = Stack()
    result = []
    tokenlist = infixexpr.split()
    for token in tokenlist:
        if token.isupper():      #Letter
            result.append(token)
        elif token == '(':
            load_Stack.push(token)
        elif token == ')':
            topToken = load_Stack.pop()
            while topToken != '(':
                result.append(topToken)
                topToken = load_Stack.pop()
        else:      #Operator
            while not load_Stack.isEmpty() and prec[load_Stack.peek()] >= prec[token]:
                result.append(load_Stack.pop())
            load_Stack.push(token)
            
    while not load_Stack.isEmpty():
        result.append(load_Stack.pop())
    return ''.join(result) 

    
#==========================================================
    

            
def infix_to_postfix(infix_expr):
    """Convert infix to postfix
       >>> infix_expr = 'A + ( ( B + C ) * ( D + E ) )'
       >>> print(infix_to_postfix(infix_expr))
       ABC+DE+*+
       >>> infix_expr = '( A + B ) * ( C + D ) * ( E + F )'
       >>> print(infix_to_postfix(infix_expr))
       AB+CD+*EF+*
    """
    prec = {}
    prec['^'] = 4
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    
    result = []
    operator_stack = Stack()
    operator_stack.push('(')
    for token in infix_expr.split() + [')']:
        if token.isupper():
            result.append(token)
        elif token == '(':
            operator_stack.push(token)
        elif token in prec:
            if prec[token] > prec[operator_stack.peek()]:
                operator_stack.push(token)
            elif prec[token] == prec[operator_stack.peek()]:
                result.append(token)
            elif prec[token] < prec[operator_stack.peek()]:
                result.append(operator_stack.pop())
        elif token == ')':
            operator = operator_stack.pop()
            while operator != '(':
                result.append(operator)
                operator = operator_stack.pop()
    
    return ''.join(result)
            
            
#=======================================================    
    
    
       
def postfix_evaluation(postfix_expr):
    """Evaluate the the postfix expression, the number must be single digit"""
    token_list = postfix_expr.split()
    load_stack = Stack()
    for token in token_list:
        if token.isdigit():
            load_stack.push(int(token))
        elif token in '+-*/':
            operand2 = load_stack.pop()
            operand1 = load_stack.pop()
            calculation = infix_evaluation(token, operand1, operand2)
            load_stack.push(calculation)
            
    return load_stack.pop()
            
          
def infix_evaluation(operator, operand1, operand2):
    """Evaluate the the infix expression, the number must be single digit"""
    if operator == '+':
        return operand1 + operand2
    if operator == '-':
        return operand1 - operand2
    if operator == '*':
        return operand1 * operand2
    if operator == '/':
        return operand1 / operand2    

print(doctest.testmod())


#======================================================
def infix_evaluator(infix_expr):
    """Convert infix to postfix and using postfix evaluator
    """
    prec = {}
    prec['^'] = 4
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    
    operator_stack = Stack()
    operand_stack = Stack()
    operator_stack.push('(')
    for token in infix_expr + ')':
        if token.isdigit():
            operand_stack.push(int(token))
        elif token == '(':
            operator_stack.push(token)
        elif token in prec:
            if prec[token] > prec[operator_stack.peek()]:
                operator_stack.push(token)
            elif prec[token] == prec[operator_stack.peek()]:
                operator_stack.push(token)
            elif prec[token] < prec[operator_stack.peek()]:
                operand_stack.push(int(token))
        elif token == ')':
            operator = operator_stack.pop()
            while operator != '(':
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                calculation = infix_evaluation(operator, operand1, operand2)                
                operand_stack.push(calculation)
                operator = operator_stack.pop()

    return operand_stack.pop()

infix_expr = '2*(4+5)'
print(infix_evaluator(infix_expr))