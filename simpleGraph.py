# Graphs
# 1 - Read from a file...NOT RECOMMENDED
# 2 - Sparse graph (each node has a list of edges)
# 3 - More Connected Graph, 2D array (edges stored in a table)

class Node:
    def __init__(self, name):
        self.name = name
        self.edges = []

class Edge:
    def __init__(self, to):
        self.to = to

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes


fort = Node("Fort")
swingset = Node("Swingset")
shed = Node("Shed")
frontyard = Node("Frontyard")
backyardNorth = Node("backyardNorth")
backyardSouth = Node("backyardSouth")

fort.edges += [swingset]
swingset.edges += [shed]
shed.edges += [backyardNorth]
backyardNorth.edges += [frontyard]
frontyard += [backyardSouth]
backyardSouth.edges += [fort]

graph = Graph([fort,swingset,shed,frontyard,backyardNorth,backyardSouth])

