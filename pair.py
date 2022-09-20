list = ["Alice", "Bob", "Carlos"]

"""
Traditional return statement
"""
def next(l, index):
  return l[index + 1]

print("next:")
print(next(list, 0))

"""
Pair class
"""
class Pair:
  def __init__(self, one, two):
    self.one = one
    self.two = two

  def __str__(self) -> str:
    return f"{self.one} and {self.two}"

def next2(l, index):
  return Pair(l[index+1], l[index+2])

print()
print("next2:")
print(next2(list, 0))

"""
A shortcut in dynamically-typed langues (like python)
"""

def next2Dynamic(l, index):
  return [l[index+1], l[index+2]]

print()
print("next2Dynamic:")
print(next2Dynamic(list, 0))
