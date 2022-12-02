class Graph:
  def __init__(self, nodes, edges):
    self.nodes = nodes
    self.edges = edges

class Node:
  def __init__(self, name):
    self.name = name
  def __repr__(self):
    return self.name
  

class WeightedEdge:
  def __init__(self, nodeA, nodeB, weight):
    self.nodeA = nodeA
    self.nodeB = nodeB
    self.weight = weight
  def __repr__(self):
    return str(self.nodeA) + " " + str(self.nodeB) + ": " + str(self.weight)

westgate = Node("Westgate")
grimsby = Node("Grimsby")
frenchyPlace = Node("FrenchyPlace")
bargate = Node("Bargate")
weelsbyRoad = Node("Weelsby Road")
cleethorpes = Node("Cleethorpes")
golfClub = Node("Golf Club")
newWaltham = Node("New Waltham")
humberston = Node("Humberston")
stationRoad = Node("StationRoad")
waltham = Node("Waltham")

nodes = [westgate, grimsby, frenchyPlace, bargate, weelsbyRoad,cleethorpes, golfClub, newWaltham, humberston, stationRoad,waltham]

edges = [
  WeightedEdge(westgate, grimsby, 1),
  WeightedEdge(westgate, cleethorpes, 5),
  WeightedEdge(grimsby,frenchyPlace, 2),
  WeightedEdge(grimsby,weelsbyRoad,2),
  WeightedEdge(frenchyPlace,bargate, 1),
  WeightedEdge(bargate,weelsbyRoad, 3),
  WeightedEdge(bargate, waltham, 5),
  WeightedEdge(weelsbyRoad, cleethorpes, 6),
  WeightedEdge(weelsbyRoad, newWaltham, 4),
  WeightedEdge(cleethorpes,golfClub, 7),
  WeightedEdge(golfClub,newWaltham,1),
  WeightedEdge(golfClub,humberston,4),
  WeightedEdge(newWaltham,stationRoad,2),
  WeightedEdge(humberston,stationRoad,5),
  WeightedEdge(stationRoad,waltham,3),
]

graph = Graph(nodes, edges)

def kruskal(graph):
  trees = {key: i for i, key in enumerate(graph.nodes)}
  msp = []
  graph.edges.sort(key=lambda x:x.weight)
  for edge in graph.edges:
    if trees[edge.nodeA] == trees[edge.nodeB]:
      continue
    msp += [edge]
    edge_1 = trees[edge.nodeB]
    for node in trees:
      if trees[node] == edge_1:
        trees[node] = trees[edge.nodeA]
    if len(list(set(list(trees.values())))) == 1:
      break
  mspSum = 0
  for edge in msp:
    mspSum += edge.weight
  print(mspSum)
  print(msp)


kruskal(graph)
