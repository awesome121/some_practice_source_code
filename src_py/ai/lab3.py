import re
from search import *


def clauses(knowledge_base):
    """Takes the string of a knowledge base; returns an iterator for pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    -- Kourosh Neshatian - 31 Jul 2019

    """
    ATOM   = r"[a-z][a-zA-z\d_]*"
    HEAD   = rf"\s*(?P<HEAD>{ATOM})\s*"
    BODY   = rf"\s*(?P<BODY>{ATOM}\s*(,\s*{ATOM}\s*)*)\s*"
    CLAUSE = rf"{HEAD}(:-{BODY})?\."
    KB     = rf"^({CLAUSE})*\s*$"

    assert re.match(KB, knowledge_base)

    for mo in re.finditer(CLAUSE, knowledge_base):
        yield mo.group('HEAD'), re.findall(ATOM, mo.group('BODY') or "")


class KBGraph(Graph):
    def __init__(self, kb, query):
        self.clauses = list(clauses(kb))
        self.query = query # e.g {'a', 'b', 'c'}
    def starting_nodes(self):
        return [self.query]
        
    def is_goal(self, node):
        if len(node) == 0:
            return True
        return False

    def outgoing_arcs(self, tail_node): # node is a set of atoms e.g. {'b', 'c'}
        arcs = []
        for atom in tail_node:
            for head, body in self.clauses: # head is an atom, body is a list of atoms
                if atom == head:
                    candidate = set(tail_node)
                    candidate.remove(atom)
                    candidate = candidate.union(set(body)) # replace
                    arcs.append(Arc(tail_node, candidate, str(tail_node)+"->"+str(candidate), 1))
        return arcs

class DFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = []

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self
        
    def __next__(self):
        if len(self.container) > 0:
            return self.container.pop()
        else:
            raise StopIteration   # don't change this one
    
    
    
    
    
    
    
    
from search import *

kb = """
a :- b, c.
b :- d, e.
b :- g, e.
c :- e.
d.
e.
f :- a,
     g.
"""
query = {'a', 'b', 'd'}
if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
    print("The query is true.")
else:
    print("The query is not provable.")


kb = """
a :- b, c.
b :- d, e.
b :- g, e.
c :- e.
d.
e.
f :- a,
     g.
"""

query = {'a'}
if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
    print("The query is true.")
else:
    print("The query is not provable.")

kb = """
all_tests_passed :- program_is_correct.
all_tests_passed.
"""

query = {'program_is_correct'}
if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
    print("The query is true.")
else:
    print("The query is not provable.")


kb = """
a :- b.
"""

query = {'c'}
if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
    print("The query is true.")
else:
    print("The query is not provable.")
