class Pair:
  def __init__(self, one, two):
    self.one = one
    self.two = two


class Map:
  items = []
  def add(self, pair):
    self.items.append(pair)
  def get(self, key):
    return next(x for x in self.items if x.one == key)

classes = Map()
classes.add(Pair(276, "Data Structures"))
classes.add(Pair(260, "Computer Graphics"))
classes.add(Pair("patio", "Recess"))

print("Which class do I have in 276?")
print(classes.get(276).two)
