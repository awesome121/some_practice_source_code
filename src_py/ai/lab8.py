network = {
    'Virus' : {
        'Parents' : [],
        'CPT' : {
            () : 0.01
        }
    },
    'A' : {
        'Parents' : ['Virus'],
        'CPT' : {
            (True,) : 0.95,
            (False,) : 0.1
        }
    },
    'B' : {
        'Parents' : ['Virus'],
        'CPT' : {
            (True,) : 0.9,
            (False,) : 0.05
        }
    }
}
import itertools
def joint_prob(network, assignment):
    p = 1 # p will enentually hold the value we are interested in
    for var in network:
        parents = network[var]['Parents']
        truth_table = tuple()
        for parent in parents:
            truth_table += (assignment[parent],)
        CPT = network[var]['CPT']
        prob = CPT[truth_table]
        if assignment[var]:
            p *= prob
        else:
            p *= (1-prob)
    return p


def query(network, query_var, evidence):
    hidden_vars = network.keys() - evidence.keys() - {query_var}
    
    if len(hidden_vars) == 0:
        
        assignments = {**evidence, **{query_var : False}}
        p_false = joint_prob(network, assignments)
        assignments = {**evidence, **{query_var : True}}
        p_true = joint_prob(network, assignments)
        return {False:p_false/(p_true+p_false), True:p_true/(p_true+p_false)}
    p_true = 0
    p_false = 0
    for values in itertools.product((True, False), repeat=len(hidden_vars)):
        assignments = {var : val for var,val in zip(hidden_vars, values)}
        
        for var in evidence:
            assignments[var] = evidence[var]
        assignments_p_false = {**assignments, **{query_var : False}}
        p_false += joint_prob(network, assignments_p_false)
        assignments_p_true = {**assignments, **{query_var : True}}
        p_true += joint_prob(network, assignments_p_true)
        #print(assignments,joint_prob(network, assignments))
        #print(p)
    #print(f"----{p}")
    return {False:p_false/(p_true+p_false), True:p_true/(p_true+p_false)}

answer = query(network, 'Virus', {'A': True})
print("The probability of carrying the virus\n"
      "if test A is positive: {:.5f}"
      .format(answer[True]))

answer = query(network, 'Virus', {'B': True})
print("The probability of carrying the virus\n"
      "if test B is positive: {:.5f}"
      .format(answer[True]))
function_symbols = ['f', '+']
leaf_symbols = ['x', 'y']
expression = 'y'

print(is_valid_expression(
        expression, function_symbols, leaf_symbols))
