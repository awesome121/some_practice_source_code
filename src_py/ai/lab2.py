from search import *
from heapq import *
import math
class LocationGraph(ExplicitGraph):
    def __init__(self, nodes, locations, edges, starting_nodes, goal_nodes):
        self.nodes = nodes
        self.locations = locations
        self.edges = edges
        self._starting_nodes = starting_nodes
        self.goal_nodes = goal_nodes

    def outgoing_arcs(self, node):
        arcs = []
        for edge in self.edges:
            if node in edge:
                tail = edge[0] if edge[0] != node else edge[1]
                cost = math.sqrt((self.locations[node][0] - self.locations[tail][0])**2\
                        + (self.locations[node][1] - self.locations[tail][1])**2)
                candidate = Arc(node, tail, str(node) + '->' + str(tail), cost) 
                if candidate not in arcs:
                    arcs.append(candidate)
        return sorted(arcs)


    def starting_nodes(self):
        return self._starting_nodes 


class LCFSFrontier(Frontier):
    def __init__(self):
        self.heap = []
    
    def add(self, path):
        #print(path)
        cost = 0
        for arc in path:
            cost += arc.cost
        heappush(self.heap, (cost, path)) # (cost, arc)

    def __next__(self):
        return heappop(self.heap)[1] # return the lowest arc's cost
graph = LocationGraph(
    nodes={'A', 'B', 'C', 'D', 'G'},
    estimates={'A':5, 'B':5, 'C':9, 'D':1, 'G':0},
    edge_list=[('A','B',2), ('A','C',3), ('B','D',5), ('C','D',10), ('D','G',3)],
    starting_nodes=['A'],
    goal_nodes={'G'},
    )

solution = next(generic_search(graph, LCFSFrontier()))
print_actions(solution)
