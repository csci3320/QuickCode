class Node:
    def __init__(self, name):
        self.name = name
        self.edges = []

class Edge:
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2

n1 = Node("SLC")
n2 = Node("ATL")
n3 = Node("OMA")
n4 = Node("SFO")

e1 = Edge(n1, n2)
e2 = Edge(n3, n2)
e3 = Edge(n4, n2)
e4 = Edge(n1, n4)

class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges

graph = Graph([n1,n2,n3,n4],[e1,e2,e3,e4])




