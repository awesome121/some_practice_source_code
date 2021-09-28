from abstract_data_type import Stack
from doctest import testmod
def infix_to_prefix(infix_expr):
    """Convert infix to prefix
    Test:
       >>> infix_expr = 'A + ( ( B + C ) * ( D + E ) )'
       >>> print(infix_to_prefix(infix_expr))
       +A*+BC+DE
       >>> infix_expr = '( A + B ) * ( C + D ) * ( E + F )'
       >>> print(infix_to_prefix(infix_expr))
       **+AB+CD+EF
    """
    prec = {}
    prec[')'] = 1
    prec['+'] = 2
    prec['-'] = 2
    prec['*'] = 3
    prec['/'] = 3
    prec['^'] = 4
    
    result = []
    opStack = Stack()
    infix_expr = ['('] + infix_expr.split() + [')']
    i = len(infix_expr) - 1
    while i != -1:
        token = infix_expr[i]
        if token.isupper():
            result.insert(0, token)
        
        elif token == ')':
            opStack.push(token)
            
        elif token == '(':
            operator = opStack.pop()
            while operator != ')':
                result.insert(0, operator)
                operator = opStack.pop()
                
        elif token in prec:
            if prec[token] >= prec[opStack.peek()]:
                opStack.push(token)
            elif prec[token] < prec[opStack.peek()]:
                operator = opStack.pop()
                result.insert(0, operator)
                opStack.push(token)
                
        i -= 1
        
    return ''.join(result)

#print(testmod())


#===========================================================
def prefix_evaluation(prefix_expr):
    """Evaluate the prefix expression
    """
    prec = {}
    prec[')'] = 1
    prec['+'] = 2
    prec['-'] = 2
    prec['*'] = 3
    prec['/'] = 3
    prec['^'] = 4    
    operands_Stack = Stack()
    i = len(prefix_expr) - 1
    while i != -1:
        token = prefix_expr[i]

        if token.isdigit():
            operands_Stack.push(int(token))
        elif token in prec:
            operand1 = operands_Stack.pop()
            operand2 = operands_Stack.pop()
            calculation = do_math(token, operand1, operand2)
            operands_Stack.push(calculation)
        i -= 1
        
    return operands_Stack.pop()

def do_math(operator, operand1, operand2):
    if operator == '+':
        return operand1 + operand2
    
    elif operator == '-':
        return operand1 - operand2
    
    elif operator == '*':
        return operand1 * operand2  
    
    elif operator == '/':
        return operand1 / operand2
    
    elif operator == '^':
        return operand1 ^ operand2    
    
prefix_expr = '++*1234'
print(prefix_evaluation(prefix_expr))




