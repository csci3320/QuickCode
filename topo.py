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
  for node in graph.nodes:
    if node.inDegree == 0:
      q.append(node)
  while q:
    v = q.pop(0)
    list.append(v)
    count += 1
    v.topNum = count
    for w in v.edges:
      w.inDegree -= 1
      if w.inDegree == 0:
        q.append(w)
 
  if count != len(graph.nodes):
    raise RuntimeError("CYCLES_FOUND_EXCEPTION")
  print([str(item) for item in list])

toposort(graph)

