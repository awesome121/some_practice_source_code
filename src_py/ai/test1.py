from assign1 import *
map_str = """\
+-------+
|  9  XG|
|X XXX  |
| S  0FG|
+-------+
"""

graph = RoutingGraph(map_str)

print("Starting nodes:", sorted(graph.starting_nodes()))
print("Outgoing arcs (available actions) at starting states:")
for s in sorted(graph.starting_nodes()):
    print(s)
    for arc in graph.outgoing_arcs(s):
        print ("  " + str(arc))

node = (1,1,5)
print("\nIs {} goal?".format(node), graph.is_goal(node))
print("Outgoing arcs (available actions) at {}:".format(node))
for arc in graph.outgoing_arcs(node):
    print ("  " + str(arc))

node = (1,7,2)
print("\nIs {} goal?".format(node), graph.is_goal(node))
print("Outgoing arcs (available actions) at {}:".format(node))
for arc in graph.outgoing_arcs(node):
    print ("  " + str(arc))

node = (3, 7, 0)
print("\nIs {} goal?".format(node), graph.is_goal(node))

node = (3, 7, math.inf)
print("\nIs {} goal?".format(node), graph.is_goal(node))

node = (3,6,5)
print("\nIs {} goal?".format(node), graph.is_goal(node))
print("Outgoing arcs (available actions) at {}:".format(node))
for arc in graph.outgoing_arcs(node):
    print ("  " + str(arc))

node = (3,6,9)
print("\nIs {} goal?".format(node), graph.is_goal(node))
print("Outgoing arcs (available actions) at {}:".format(node))
for arc in graph.outgoing_arcs(node):
    print ("  " + str(arc))
