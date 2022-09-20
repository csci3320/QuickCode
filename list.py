class List:
  items = []
  def add(self, value):
    self.items.append(value)
  def getAt(self, index):
    return self.items[index]

favoriteMovies = List()
favoriteMovies.add("Casablanca")
favoriteMovies.add("The first Thor movie")
favoriteMovies.add("The Harry Potter movie where Dumbledore dies")

print("What is my most favorite movie")
print(favoriteMovies.getAt(0))
print("What is my next favorite movie?")
print(favoriteMovies.getAt(1))

