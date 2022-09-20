class Node:
  def __init__(self, name):
    self.name = name
    self.links = []
  def addLink(self, link):
    self.links.append(link)
    link.links.append(self)
  

class Graph:
  def __init__(self, root):
    self.root = root

oma = Node("Omaha Airport")
sfo = Node("San Francisco Airport")
atl = Node("Atlanta Airport")
ord = Node("Chicago Airport")

oma.addLink(atl)
sfo.addLink(atl)
ord.addLink(atl)
ord.addLink(sfo)

omahaFlights = Graph(oma)
atlantaFlights = Graph(atl)

print(f"From Omaha I can fly to:")
for node in omahaFlights.root.links:
  print(node.name)
print()

print(f"From Atlanta I can fly to:")
for node in atlantaFlights.root.links:
  print(node.name)



