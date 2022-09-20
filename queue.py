class Queue:
  items = []
  def add(self, value):
    self.items.append(value)
  def popFront(self):
    if len(self.items) == 0:
      return None
    return self.items.pop(0)

emails = Queue()
emails.add("From family")
emails.add("From friends")
emails.add("Spam")

print("Reading emails:")

while True:
  next = emails.popFront()
  if next == None:
    break
  print(next)