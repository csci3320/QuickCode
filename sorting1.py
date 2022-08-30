data = [3,2,5,8,9,1,0,22,31, 4, 19, 100, 145, 169, 133, 11, 12, 14, 13,7,6]
short = [3,2,1]
def bubbleSortSlow(list):
  ticks = 0
  for i in range(0, len(list)):
    for j in range(0, len(list)-1):
      ticks += 1
      if list[j] > list[j+1]:
        temp = list[j]
        list[j] = list[j+1]
        list[j+1] = temp
  return ticks

def bubbleSortFast(list):
  ticks = 0
  for i in range(0, len(list)):
    for j in range(0, len(list)-1-i):
      ticks += 1
      if list[j] > list[j+1]:
        temp = list[j]
        list[j] = list[j+1]
        list[j+1] = temp
  return ticks

def selectionSort(list):
  ticks = 0
  for head in range(0, len(list)):
    smallest = 100000
    index = -1
    for candidate in range(head, len(list)):
      ticks += 1
      if list[candidate] < smallest:
        index = candidate
        smallest = list[candidate]
    temp = list[head]
    list[head] = smallest
    list[index] = temp
  return ticks

def insertionSort(list):
  ticks = 0
  for head in range(0, len(list)):
    value = list[head]
    for j in range(head, -1, -1):
      ticks += 1
      if j == 0:
        list[0] = value
        break
      if list[j-1] < value:
        list[j] = value
        break
      else:
        list[j] = list[j-1]
  return ticks





print(insertionSort(data.copy()))

print("Count BubbleSlow BubbleFast Selection")
for i in range(1, len(data)):
  tempList = data[:i]
  first = bubbleSortSlow(tempList.copy())
  second = bubbleSortFast(tempList.copy())
  third = selectionSort(tempList.copy())
  forth = insertionSort(tempList.copy())
  print(f"{i} {first} {second} {third} {forth}")
