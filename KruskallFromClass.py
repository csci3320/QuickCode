class Node:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
    def __repr__(self):
        return str(self)

class Edge:
    def __init__(self, nodeA, nodeB, weight):
        self.nodeA = nodeA
        self.nodeB = nodeB
        self.weight = weight
    def __repr__(self):
        return "" + str(self.nodeA) + " " + str(self.nodeB) + " " + str(self.weight)

omaha = Node("Omaha")
lincoln = Node("Lincoln")
grandIsland = Node("Grand Island")
siouxCity = Node("Sioux City")
kansasCity = Node("Kansas City")

nodes = [omaha, lincoln, siouxCity, grandIsland, kansasCity]

omahaLincoln = Edge(omaha, lincoln, 50)
omahaSiouxCity = Edge(omaha, siouxCity, 100)
omahaKansasCity = Edge(omaha, kansasCity, 250)
lincolnSiouxCity = Edge(lincoln, siouxCity, 120)
lincolnGrandIsland = Edge(lincoln, grandIsland, 150)
lincolnKansasCity = Edge(lincoln, kansasCity, 260)
siouxCityKansasCity = Edge(siouxCity, kansasCity, 400)
grandIslandSiouxCity = Edge(grandIsland, siouxCity, 200)
grandIslandKansasCity = Edge(grandIsland, kansasCity, 175)

edges = [omahaLincoln, omahaSiouxCity, omahaKansasCity, lincolnSiouxCity, lincolnKansasCity, lincolnGrandIsland, siouxCityKansasCity, grandIslandKansasCity, grandIslandSiouxCity]

tempTrees = {omaha:0, lincoln:1, siouxCity:2, grandIsland:3, kansasCity:4}

msp = []

cont = True
while(cont and len(edges) > 0):
    cont = False
    minDistance = 872
    minIndex = -1
    for i in range(len(edges)):
        if edges[i].weight < minDistance:
            minDistance = edges[i].weight
            minIndex = i

    edge = edges.pop(minIndex)
    nodeA = edge.nodeA
    nodeB = edge.nodeB
    nodeATree = tempTrees[nodeA]
    nodeBTree = tempTrees[nodeB]
    if nodeATree == nodeBTree:
        cont = True
        continue
    #implied else
    msp += [edge]
    for node in tempTrees:
        if tempTrees[node] == nodeBTree:
            tempTrees[node] = nodeATree
            cont = True

print(msp)



