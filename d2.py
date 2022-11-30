class Graph:
  def __init__(self, nodes):
    self.nodes = nodes
  def addEdge(self, start, end):
    next(x for x in self.nodes if x is start).edges += [end]
  def hasEdgeTo(self, start, end):
    return end in map(lambda x:x.node, start.edges)
  def getEdgeTo(self, start, end):
    return next(x for x in start.edges if x.node is end)

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

#Find connection from a to c
dictionary = {a:0,b:1000, c:1000}
finalizedNodes = [a]

# loop if finalizedNodes is the same size as the number of nodes
# Grab the last finalized node
# Loop over all the nodes in the graph
# Skip those that are finalized
# See if base connects to that node
# If so, get that edge
# Get the weight on the edge
# If the weight is less than that in the dictionary
# Update the dictionary to the be the weight 
# plus the distance to base
# Find the remaining node with the shortest distance
# Add shortest distance node as the most recent finalized node
  

print("The shortest route to b is: " + str(dictionary[b]))
