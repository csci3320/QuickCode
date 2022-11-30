class DirectedGraph:
  def __init__(self, nodes):
    self.nodes = nodes
  def updateAll(self):
    for node in self.nodes:
      node.outDegree = len(node.edges)
      for node2 in self.nodes:
        if node is node2:
          continue
        if node2.hasEdgeTo(node):
          node.inDegree += 1
        

class Node:
  def __init__(self, value):
    self.value = value
    self.outDegree = 0
    self.inDegree = 0
    self.edges = []

  def addEdgeTo(self, node):
    self.edges.append(node)

  def hasEdgeTo(self, otherNode):
    for edge in self.edges:
      if edge is otherNode:
        return True
    return False

  def __str__(self):
    return str(self.value)

  def __repr__(self):
    return str(self.value)

v1 = Node("v1")
v2 = Node("v2")
v3 = Node("v3")
v4 = Node("v4")
v5 = Node("v5")
v6 = Node("v6")
v7 = Node("v7")

v1.addEdgeTo(v2)
v1.addEdgeTo(v3)
v1.addEdgeTo(v4)
v2.addEdgeTo(v4)
v2.addEdgeTo(v5)
v3.addEdgeTo(v6)
v4.addEdgeTo(v3)
v4.addEdgeTo(v6)
v4.addEdgeTo(v7)
v5.addEdgeTo(v4)
v5.addEdgeTo(v7)
v7.addEdgeTo(v6)

graph = DirectedGraph([v1,v2,v3,v4,v5,v6,v7])
graph.updateAll()



def toposort(graph):

  q = []
  count = 0
  list = []
  # loop through all the nodes and add the ones that have an indegree of 0
  # loop while q is not of length 0
  # get the vertex by popping 0
  # add the popped vertex to the list
  # increment count
  # loop over popped vertex's edges
  # Subtract 1 from those edges in degrees
  # If the indegree is 0
  # Adding to q
  
  print([str(item) for item in list])

toposort(graph)

