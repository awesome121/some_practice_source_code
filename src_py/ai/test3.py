from assign1 import *

from search import *

#map_str = """\
#+-------+
#|   G   |
#|       |
#|   S   |
#+-------+
#"""
#
#map_graph = RoutingGraph(map_str)
#frontier = AStarFrontier(map_graph)
#solution = next(generic_search(map_graph, frontier), None)
#print_actions(solution)
#
#
#map_str = """\
#+-------+
#|  GG   |
#|S    G |
#|  S    |
#+-------+
#"""
#
#map_graph = RoutingGraph(map_str)
#frontier = AStarFrontier(map_graph)
#solution = next(generic_search(map_graph, frontier), None)
#print_actions(solution)
#
#map_str = """\
#+-------+
#|     XG|
#|X XXX  |
#| S     |
#+-------+
#"""
#
#map_graph = RoutingGraph(map_str)
#frontier = AStarFrontier(map_graph)
#solution = next(generic_search(map_graph, frontier), None)
#print_actions(solution)
#
#
#map_str = """\
#+-------+
#|  F  X |
#|X XXXXG|
#| 3     |
#+-------+
#"""
#
#map_graph = RoutingGraph(map_str)
#frontier = AStarFrontier(map_graph)
#solution = next(generic_search(map_graph, frontier), None)
#print_actions(solution)
#
#
#map_str = """\
#+--+
#|GS|
#+--+
#"""
#map_graph = RoutingGraph(map_str)
#frontier = AStarFrontier(map_graph)
#solution = next(generic_search(map_graph, frontier), None)
#print_actions(solution)
#
#
#map_str = """\
#+---+
#|GF2|
#+---+
#"""
#map_graph = RoutingGraph(map_str)
#frontier = AStarFrontier(map_graph)
#solution = next(generic_search(map_graph, frontier), None)
#print_actions(solution)
#
#
#map_str = """\
#+----+
#| S  |
#| SX |
#|GX G|
#+----+
#"""
#
#map_graph = RoutingGraph(map_str)
#frontier = AStarFrontier(map_graph)
#solution = next(generic_search(map_graph, frontier), None)
#print_actions(solution)

map_str = """\
+----------------+
|2              F|
|XX     G 123    |
|3XXXXXXXXXXXXXX |
|  F             |
|          F     |
+----------------+
"""
map_graph = RoutingGraph(map_str)
frontier = AStarFrontier(map_graph)
solution = next(generic_search(map_graph, frontier), None)
print_actions(solution)


map_str = """\
+---------+
|         |
|    G    |
|         |
+---------+
"""

map_graph = RoutingGraph(map_str)
frontier = AStarFrontier(map_graph)
solution = next(generic_search(map_graph, frontier), None)
print_actions(solution)
