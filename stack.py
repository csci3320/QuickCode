class Stack:
  values = []
  def add(self, value):
    self.values.append(value)
  def pop(self):
    if len(self.values) == 0:
      return None
    return self.values.pop()

trunk = Stack()
trunk.add("Paper Towels")
trunk.add("Cereal")
trunk.add("Bags of Candy")

print("Unloading:")
while True:
  next = trunk.pop()
  if next == None:
    break
  print(next)
