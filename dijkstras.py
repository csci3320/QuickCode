class Graph:
  def __init__(self, nodes):
    self.nodes = nodes
  def addEdge(self, start, end):
    next(x for x in self.nodes if x is start).edges += [end]
  def hasEdgeTo(self, start, end):
    return end in map(lambda x:x.node, start.edges)
  def getEdgeTo(self, start, end):
    return next(x for x in start.edges if x.node is end)
  
  

class Graph2:
  def __init__(self, nodes):
    size = len(nodes)
    self.nodes = nodes
    self.table = [[None for x in range(size)] for y in range(size)]

class Node:
  def __init__(self, name):
    self.name = name
    self.edges = []
  def addEdge(self, edge):
    self.edges += [edge]
  def hasEdgeTo(self, node):
    return node in map(lambda x:x.node, self.edges)
  def getEdgeTo(self, node):
    return next(x for x in self.edges if x.node is node)

class WeightedEdge:
  def __init__(self, node, weight):
    self.node = node
    self.weight = weight

a = Node("a")
b = Node("b")
c = Node("c")

a.addEdge(WeightedEdge(b, 10))
a.addEdge(WeightedEdge(c, 1))
c.addEdge(WeightedEdge(b, 1))

graph = Graph([a,b,c])
graph2 = Graph([a,b,c])

#Find connection from a to c
dictionary = {a:0,b:1000, c:1000}
finalizedNodes = [a]

madeChange = True
while(madeChange):
  madeChange = False
  base = finalizedNodes[-1]
  for node in graph.nodes:
    if node in finalizedNodes:
      continue
    if base.hasEdgeTo(node):
      edge = base.getEdgeTo(node)
      weight = edge.weight
      if weight < dictionary[node]:
        dictionary[node] = weight + dictionary[base]
  
  shortest = 100
  shortestNode = None
  for node in graph.nodes:
    if node in finalizedNodes:
      continue
    if dictionary[node] < shortest:
      shortest = dictionary[node]
      shortestNode = node
  if shortestNode is not None:
    madeChange = True
    finalizedNodes += [shortestNode]

print("The shortest route to b is: " + str(dictionary[b]))
