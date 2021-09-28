from csp import *

#def generate_and_test(csp):
#    names, domains = zip(*csp.var_domains.items())
#    for values in itertools.product(*domains):
#        assignment = {x: v for x, v in zip(names, values)}
#        if all(satisfies(assignment, constraint) for constraint in list(csp.constraints)):
#            yield assignment
#
#simple_csp = CSP(
#    var_domains={x: set(range(1, 5)) for x in 'abc'},
#    constraints={
#        lambda a, b: a < b,
#        lambda b, c: b < c,
#        })
#
#canterbury_colouring = CSP(
#    var_domains={
#        'christchurch': {'red', 'green'},
#        'selwyn': {'red', 'green'},
#        'waimakariri': {'red', 'green'},
#        },
#    constraints={
#        lambda christchurch, waimakariri: christchurch != waimakariri,
#        lambda christchurch, selwyn: christchurch != selwyn,
#        lambda selwyn, waimakariri: selwyn != waimakariri,
#        })

#import itertools, copy
#from csp import *
#
#def arc_consistent(csp):
#    csp = copy.deepcopy(csp)
#    to_do = {(x, c) for c in csp.constraints for x in csp.var_domains} # COMPLETE
#    while to_do:
#        x, c = to_do.pop()
#        ys = scope(c) - {x}
#        new_domain = set()
#        for xval in csp.var_domains[x]: # COMPLETE
#            assignment = {x: xval}
#            for yvals in itertools.product(*[csp.var_domains[y] for y in ys]):
#                assignment.update({y: yval for y, yval in zip(ys, yvals)})
#                if satisfies(assignment, c): # COMPLETE
#                    new_domain.add(xval) # COMPLETE
#                    break
#        if csp.var_domains[x] != new_domain:
#            for cprime in set(csp.constraints) - {c}:
#                if x in scope(cprime):
#                   for z in scope(cprime): # COMPLETE
#                       if x != z: # COMPLETE
#                           to_do.add((z, cprime))
#            csp.var_domains[x] = new_domain     #COMPLETE
#    return csp
#
#csp = CSP(
#   var_domains = {var:{0,1,2} for var in 'abcd'},
#   constraints = {
#      lambda a, b, c: a > b + c,
#      #lambda c, d: c > d
#      }
#   )
#
#print(arc_consistent(csp).var_domains)






import itertools, copy 
from csp import scope, satisfies, CSP

def generate_and_test(csp):
    names, domains = zip(*csp.var_domains.items())
    for values in itertools.product(*domains):
        assignment = {x: v for x, v in zip(names, values)}
        if all(satisfies(assignment, constraint) for constraint in list(csp.constraints)):
            yield assignment
    
def arc_consistent(csp):
    csp = copy.deepcopy(csp)
    to_do = {(x, c) for c in csp.constraints for x in csp.var_domains} # COMPLETE
    while to_do:
        x, c = to_do.pop()
        ys = scope(c) - {x}
        new_domain = set()
        for xval in csp.var_domains[x]: # COMPLETE
            assignment = {x: xval}
            for yvals in itertools.product(*[csp.var_domains[y] for y in ys]):
                assignment.update({y: yval for y, yval in zip(ys, yvals)})
                if satisfies(assignment, c): # COMPLETE
                    new_domain.add(xval) # COMPLETE
                    break
        if csp.var_domains[x] != new_domain:
            for cprime in set(csp.constraints) - {c}:
                if x in scope(cprime):
                   for z in scope(cprime): # COMPLETE
                       if x != z: # COMPLETE
                           to_do.add((z, cprime))
            csp.var_domains[x] = new_domain     #COMPLETE
    return csp

domains = {x: set(range(10)) for x in "twofur"}
domains.update({'c1':{0, 1}, 'c2': {0, 1}}) # domains of the carry overs

cryptic_puzzle = CSP(
    var_domains=domains,
    constraints={
         lambda o, r, c1    :      o + o == r + 10 * c1, # one of the constraints
        lambda w, u, c1, c2:      w + w + c1 == u + 10*c2,
        lambda t, o, c2, f:       t + t + c2 == o + 10*f,
        lambda t:               t != 0,
        lambda f:               f != 0,
        lambda t, w, o, f, u, r:  len({t, w, o, f, u, r}) == 6
        })



print(set("twofur") <= set(cryptic_puzzle.var_domains.keys()))
print(all(len(cryptic_puzzle.var_domains[var]) == 10 for var in "twour")) 


new_csp = arc_consistent(cryptic_puzzle)
print(sorted(new_csp.var_domains['r']))

new_csp = arc_consistent(cryptic_puzzle)
print(sorted(new_csp.var_domains['w']))

new_csp = arc_consistent(cryptic_puzzle)
solutions = []
for solution in generate_and_test(new_csp):
    solutions.append(sorted((x, v) for x, v in solution.items()
                            if x in "twofur"))
print(len(solutions))
solutions.sort()
print(solutions[0])
print(solutions[5])


