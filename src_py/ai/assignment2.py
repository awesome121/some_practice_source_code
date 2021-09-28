def is_valid_expression(expr, function_symbols, leaf_symbols):
    if type(expr) == int:
        return True
    elif type(expr) == str and expr in leaf_symbols:
        return True
    elif type(expr) == list and len(expr) == 3 and expr[0] in function_symbols:
        return is_valid_expression(expr[1], function_symbols, leaf_symbols)\
        and is_valid_expression(expr[2], function_symbols, leaf_symbols)
    else:
        return False

def depth(expr):
   if type(expr) != list:
       return 0
   return 1 + max(depth(expr[1]), depth(expr[2]))

def evaluate(expr, bindings):
    if type(expr) == int:
        return expr
    elif type(expr) == str:
        return bindings[expr]
    else:
        return bindings[expr[0]](evaluate(expr[1], bindings), evaluate(expr[2], bindings))

from random import random
def is_leaf():
    return int(random() * 10) % 2

def random_num(num):
    return int(random() * 10) % num
def random_expression(function_symbols, leaves, max_depth):
    result = []
    if max_depth == 0:
        return leaves[random_num(len(leaves))]
    else:
        if is_leaf():
            return leaves[random_num(len(leaves))]
        else:
            result = []
            return [function_symbols[random_num(len(function_symbols))],\
            random_expression(function_symbols, leaves, max_depth-1), \
            random_expression(function_symbols, leaves, max_depth-1)]


function_symbols = ['f', 'g', 'h']
constant_leaves =  list(range(-2, 3))
variable_leaves = ['x', 'y', 'i']
leaves = constant_leaves + variable_leaves
max_depth = 4

for _ in range(10000):
    expression = random_expression(function_symbols, leaves, max_depth)
    if not is_valid_expression(expression, function_symbols, leaves):
        print("The following expression is not valid:\n", expression)
        break
else:
    print("OK")
