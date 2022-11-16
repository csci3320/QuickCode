class Node:
    def __init__(self, name):
        self.name = name
        self.edges = []


n1 = Node("SLC")
n2 = Node("ATL")
n3 = Node("OMA")
n4 = Node("SFO")

n1.edges += [n2]
n3.edges += [n2]
n4.edges += [n2]
n1.edges += [n4]

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes

    def makeUndirected(self):
        for node in self.nodes:
            for node2 in self.nodes:
                if node is node2:
                    continue
                #Implied else
                for edge in node.edges:
                    if edge not in node2.edges:
                        node2.edges += [edge]

        

graph = Graph([n1,n2,n3,n4])
graph.makeUndirected()

print(n1 in n2.edges)




