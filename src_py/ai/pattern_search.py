from random import random
def is_leaf():
    return int(random() * 10) % 2

def random_num(num):
    return int(random() * 10) % num


def random_expression(function_symbols, leaves, max_depth):
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
        
def evaluate(expr, bindings):
    if type(expr) == int:
        return expr
    elif type(expr) == str:
        return bindings[expr]
    else:
        return bindings[expr[0]](evaluate(expr[1], bindings), evaluate(expr[2], bindings))



def generate_rest(initial_sequence, expression, length):
    bindings = {'+' : lambda x,y: x+y, '-' : lambda x,y: x-y, '*' : lambda x,y: x*y, \
        "i": len(initial_sequence), 'x': initial_sequence[-2], 'y': initial_sequence[-1]\
    }
    result = []
    for _ in range(length):
        result.append(evaluate(expression, bindings))
        if len(result) == 1:
            bindings['x'] = initial_sequence[-1]
            bindings['y'] = result[0]
        else:
            bindings['x'] = result[-2]
            bindings['y'] = result[-1]
        bindings['i'] += 1
    return result

def predict_rest(sequence):
    func = ['+', '-', '*']
    leaves = ['x', 'y', 'i'] + list(range(-2, 3))
    max_depth = 3
    bindings = {'+' : lambda x,y: x+y, '-' : lambda x,y: x-y, '*' : lambda x,y: x*y,\
                'x':sequence[0], 'y':sequence[1], 'i':2}
    cache = set()
    expr = None
    count = 0
    while not expr:
        expr = random_expression(func, leaves, 3)
        count += 1
        for i in range(2, len(sequence)-1):
            if sequence[i] != evaluate(expr, bindings):
                expr = None
                bindings['x'] = sequence[0]
                bindings['y'] = sequence[1]
                bindings['i'] = 2                  
                break
            else:
                bindings['x'] = sequence[i-1]
                bindings['y'] = sequence[i]
                bindings['i'] += 1
    return generate_rest(sequence, expr, 5)



sequence = [0, 1, 2, 3, 4, 5, 6, 7]
the_rest = predict_rest(sequence)
print(sequence)
print(the_rest)
