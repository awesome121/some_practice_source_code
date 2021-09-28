from search import *
from heapq import *
import math

STEPS = [('N' , -1, 0),
 ('E' ,  0, 1),
 ('S' ,  1, 0),
 ('W' ,  0, -1),]

def proccess_graph_str(map_str):
    """Function to extract starting nodes given map_str"""
    lines = map_str.splitlines()
    starting_nodes = []
    goal_nodes = []
    obstacles = []
    fuels = []
    row = 1
    for line in lines[1:-1]:
        col = 1
        for cell in line[1:-1]:
            if cell == 'S':
                starting_nodes.append((row, col, math.inf))    
            elif cell.isdigit():
                starting_nodes.append((row, col, int(cell)))    
            elif cell == 'G':
                goal_nodes.append((row, col))
            elif cell == 'X':
                obstacles.append((row, col))
            elif cell == 'F':
                fuels.append((row, col))
            col += 1
        row += 1
    return starting_nodes, goal_nodes, obstacles, fuels


class RoutingGraph(Graph):
    """This graph represents the routing problem"""
    def __init__(self, map_str):
        self._map_str = map_str
        self._starting_nodes, self._goal_nodes, \
                self._obstacles, self._fuels\
                = proccess_graph_str(map_str)
        self._row_limit = len(map_str.splitlines()) - 1
        self._col_limit = len(map_str.splitlines()[0]) - 1

    def starting_nodes(self):
        return self._starting_nodes

    def is_goal(self, node):
        for row, col in self._goal_nodes:
            if node[0] == row and node[1] == col:
                return True
        return False

    def is_inside(self, node):
        """Return True if it's inside the wall"""
        return 0 < node[0] < self._row_limit\
                and 0 < node[1] < self._col_limit

    def outgoing_arcs(self, node):
        arcs = []
        for action, row_off, col_off in STEPS:
            head = (node[0]+row_off, node[1]+col_off, node[2]-1)
            if self.is_inside(head[0:2])\
                    and head[0:2] not in self._obstacles\
                    and head[2] >= 0:
                arcs.append(Arc(node, head, action, 5))
        if node[0:2] in self._fuels and node[2] < 9:
            arcs.append(Arc(node, node[0:2]+(9,), 'Fuel up', 15))
        return arcs

    def estimated_cost_to_goal(self, node):
        result = []
        for goal in self._goal_nodes:
            result.append((abs(goal[0]-node[0])+abs(goal[1]-node[1]))*5)
        return min(result)
       

class AStarFrontier(Frontier):
    def __init__(self, routing_map):
        self.heap = []
        self.expanded_states = set()
        self.routing_map = routing_map

    def add(self, path):
        if path[-1][1] not in self.expanded_states:
            cost = 0
            for arc in path:
                cost += arc.cost
            cost += self.routing_map.estimated_cost_to_goal(path[-1][1])
            heappush(self.heap, (cost, self.get_entry_count(cost), path))

    def get_entry_count(self, entry_cost):
        max_count = 0
        for cost, count, _ in self.heap:
            if cost == entry_cost and count > max_count:
                max_count = count
        return max_count + 1

    def __next__(self):
        if len(self.heap) == 0:
            raise StopIteration
        else:
            _, count, path = heappop(self.heap)
            node = path[-1].head
            while node in self.expanded_states:
                if len(self.heap) == 0:
                    raise StopIteration
                path = heappop(self.heap)[-1]
                node = path[-1].head
             
            self.expanded_states.add(node)
            return path # return lowest arc's path


def print_map(map_graph, frontier, solution_path):
    if solution_path is None:
        solution_path = []
    starting_nodes = [(row, col) for (row, col, _) in map_graph._starting_nodes]
    solution_nodes = [(head[0], head[1]) for (_, head, _, _) in solution_path[1:-1]]
    expanded_nodes = [(row, col) for (row, col, _) in frontier.expanded_states]
    print('+' + '-' * (map_graph._col_limit-1) + '+')
    for row in range(1, map_graph._row_limit):
        for col in range(map_graph._col_limit+1):
            if col == 0 or col == map_graph._col_limit:
                print('|', end='')
            elif (row, col) in starting_nodes: 
                print('S', end='')
            elif (row, col) in map_graph._goal_nodes:
                print('G', end='')
            elif (row, col) in solution_nodes:
                print('*', end='')
            elif (row, col) in expanded_nodes:
                print('.', end='')
            elif (row, col) in map_graph._obstacles:
                print('X', end='')
            else:
                print(' ', end='')
        print()

    print('+' + '-' * (map_graph._col_limit-1) + '+')




