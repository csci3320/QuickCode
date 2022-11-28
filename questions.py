# Graphs
# 1 - Read from a file...NOT RECOMMENDED
# 2 - Sparse graph (each node has a list of edges)
# 3 - More Connected Graph, 2D array (edges stored in a table)

class Node:
    def __init__(self, name):
        self.name = name
        self.edges = []

class Edge:
    def __init__(self, to, answer):
        self.to = to
        self.answer = answer

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes


start = Node("How many children do you have?")
hotrod = Node("Lambo")
minivan = Node("Sienna")

eStartHotrod = Edge(hotrod, "0 or less")
eStartMinivan = Edge(minivan, "1 or more")

start.edges += [eStartHotrod]
start.edges += [eStartMinivan]

graph = Graph([start, hotrod, minivan])

print(graph.nodes[0].name)
for edge in graph.nodes[0].edges:
    print(edge.answer)




