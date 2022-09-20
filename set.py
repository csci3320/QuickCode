class Set:
  items = []
  def add(self, value):
    if value not in self.items:
      self.items.append(value)
  def __str__(self):
    return str(self.items)

goals = Set()
goals.add("Climb Mount Everest")
goals.add("See Paris")
goals.add("See Paris")

print(goals)