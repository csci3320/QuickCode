class Heap:
  def __init__(self):
    self.values = [None] * 100
    self.size = 0

  def add(self, value):
    # Now percolate up
    hole = self.size
    self.size += 1
    while hole > 0 and value < self.values[int(hole/2)]:
      self.values[hole] = self.values[int(hole/2)]
      hole = int(hole/2)
    self.values[hole] = value

  def pop(self):
    if self.size == 0: return

    toReturn = self.values[0]
    self.values[0] = self.values[self.size-1]
    self.size-=1

    r = 0
    c = 1
    n = self.size

    c = 2*r+1
    while c < n:
      if c < n-1 and self.values[c] > self.values[c+1]:
        c+= 1
      if self.values[r] > self.values[c]:
        x = self.values[r]
        self.values[r] = self.values[c]
        self.values[c] = x
        r = c
        c = c * 2
      else:
        break
      c += 1


    return toReturn
    

  def print(self):
    row = 0
    rowLength = 2**row
    
    i = 0
    thisRow = 0
    while i < self.size:
      print(self.values[i], end = ",")
      i += 1
      thisRow+=1
      if thisRow >= rowLength:
        row += 1
        print()
        rowLength = 2**row
        thisRow = 0



heap = Heap()
heap.add(1)
heap.add(2)
heap.add(0)
heap.add(3)
heap.add(5)
heap.add(20)
heap.add(4)
heap.add(10)
heap.add(6)
heap.add(30)
heap.add(7)
heap.print()

while heap.size > 0:
  
  print()
  print()
  heap.pop()
  heap.print()


