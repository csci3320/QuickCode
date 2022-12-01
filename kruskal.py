westgate = "Westgate"
grimsby = "Grimsby"
frenchyPlace = "FrenchyPlace"
bargate = "Bargate"
weelsbyRoad = "Weelsby Road"
cleethorpes = "Cleethorpes"
golfClub = "Golf Club"
newWaltham = "New Waltham"
humberston = "Humberston"
stationRoad = "StationRoad"
waltham = "Waltham"

nodes = [westgate, grimsby, frenchyPlace, bargate, weelsbyRoad,cleethorpes, golfClub, newWaltham, humberston, stationRoad,waltham]
edges = [
  [westgate, grimsby, 1],
  [westgate, cleethorpes, 5],
  [grimsby,frenchyPlace, 2],
  [grimsby,weelsbyRoad,2],
  [frenchyPlace,bargate, 1],
  [bargate,weelsbyRoad, 3],
  [bargate, waltham, 5],
  [weelsbyRoad, cleethorpes, 6],
  [weelsbyRoad, newWaltham, 4],
  [cleethorpes,golfClub, 7],
  [golfClub,newWaltham,1],
  [golfClub,humberston,4],
  [newWaltham,stationRoad,2],
  [humberston,stationRoad,5],
  [stationRoad,waltham,3],
]

def kruskal():
  trees = {key: i for i, key in enumerate(nodes)}
  msp = []
  edges.sort(key=lambda x:x[2])
  for edge in edges:
    if trees[edge[0]] == trees[edge[1]]:
      continue
    msp += [edge]
    for node in trees:
      if trees[node] == trees[edge[1]]:
        trees[node] = trees[edge[0]]
    if len(list(set(list(trees.values())))) == 1:
      break
  print(msp)


kruskal()
