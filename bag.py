class Bag:
  items = []
  def add(self, value):
    self.items.append(value)

shoppingCart = Bag()

shoppingCart.add("Milk")
shoppingCart.add("Bread")
shoppingCart.add("Bread")

print(shoppingCart.items)
