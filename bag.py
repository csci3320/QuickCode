class Bag:
  items = []
  def add(self, value):
    self.items.append(value)
    
  def __str__(self):
    return str(self.items)

shoppingCart = Bag()

shoppingCart.add("Milk")
shoppingCart.add("Bread")
shoppingCart.add("Bread")

print(shoppingCart)
