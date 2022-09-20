"""
Example of how boxing works in python
"""

print("Without boxing")
a = 1
b = a
a += 1
print(f"a={a}")
print(f"b={b}")

print()
print("With boxing")

"""
A simple box class
"""
class Box():
  def __init__(self, value):
    self.value=value

a = Box(1)
b = a
a.value += 1
print(f"a={a.value}")
print(f"b={b.value}")
