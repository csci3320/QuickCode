# List of Edges
edges = [
  {"a":"Westgate", "b": "Grimsby", "weight":1},
  {"a":"Westgate", "b": "Cleethorpes", "weight":5},
  {"a":"Grimsby", "b": "Frenchy Place", "weight":2},
  {"a":"Grimsby", "b": "Weelsby Road", "weight":2},
  {"a":"Frenchy Place", "b": "Bargate", "weight":1},
  {"a":"Bargate", "b": "Weelsby Road", "weight":3},
  {"a":"Bargate", "b": "Waltham", "weight":5},
  {"a":"Weelsby Road", "b": "Cleethorpes", "weight":6},
  {"a":"Weelsby Road", "b": "New Waltham", "weight":4},
  {"a":"Cleethorpes", "b": "Golf Club", "weight":7},
  {"a":"Golf Club", "b": "New Waltham", "weight":1},
  {"a":"Golf Club", "b": "Humberston", "weight":4},
  {"a":"New Waltham", "b": "Station Road", "weight":2},
  {"a":"Humberston", "b": "Station Road", "weight":5},
  {"a":"Station Road", "b": "Waltham", "weight":3},
]

# The list of nodes is the set of all the names in position "a" or "b"
nodes = set(list(map(lambda x:x["a"], edges)) + list(map(lambda x:x["b"], edges)))
# Create a dictionary where each key is a node and the value is a unique integer
trees = {key: i for i, key in enumerate(nodes)}
# Collection of edges that make the minimum spanning tree
msp = []
# Sort the keys so that the shortest edges come first
edges.sort(key=lambda x:x["weight"])

# Now create the msp
for edge in edges:
  # If the nodes are already connected, then skip
  if trees[edge["a"]] == trees[edge["b"]]:
    continue
  # Otherwise add it to the msp
  msp += [edge]

  #Update the nodes in our tree
  b = trees[edge["b"]]
  for node in trees:
    # If you are a node with a tree number equal to the destination node
    # update your tree number to that of the origin node
    if trees[node] == b:
      trees[node] = trees[edge["a"]]
  # Check to see if all nodes are in the same tree 
  if len(list(set(list(trees.values())))) == 1:
    break

# Print the results
print()
mspSum = 0
for edge in msp:
  mspSum += edge["weight"]
print(mspSum)
print(msp)

