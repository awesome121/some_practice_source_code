from assign1 import *
map_str = """\
+--+
|GS|
+--+
"""

graph = RoutingGraph(map_str)

print("Starting nodes:", sorted(graph.starting_nodes()))
print("Outgoing arcs (available actions) at the start:")
for start in graph.starting_nodes():
    for arc in graph.outgoing_arcs(start):
        print ("  " + str(arc))



node = (1,1,1)
print("\nIs {} goal?".format(node), graph.is_goal(node))
print("Outgoing arcs (available actions) at {}:".format(node))
for arc in graph.outgoing_arcs(node):
    print ("  " + str(arc))


print("-"*10)

map_str = """\
+------+
|S    S|
|  GXXX|
|S     |
+------+
"""

graph = RoutingGraph(map_str)
print("Starting nodes:", sorted(graph.starting_nodes()))
