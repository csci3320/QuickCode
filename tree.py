class Person:
  mother = None
  father = None
  name = None
  def __init__(self, name, mother, father):
    (self.name, self.mother, self.father) = (name, mother, father)

class Tree:
  root = None
  def __init__(self, root):
    self.root = root


pop = Person("James", None, None)
mum = Person("Lilly", None, None)
harry = Person("Harry", mum, pop)
familyTree = Tree(harry)

print("About me:")
print(f"My name is {familyTree.root.name}")
print(f"My mother's name is {familyTree.root.mother.name}")
print(f"My father's name is {familyTree.root.father.name}")
 

