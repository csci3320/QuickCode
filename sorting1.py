import math # We use math.floor in merge sort when we find the center index

"""
This code creates a table of approximate run times for several sorting algorithms
Each algorithm returns the number of ticks.
"""


# Longer data used in the table
data = [3, 2, 5, 8, 9, 1, 0, 22, 31, 4, 19,100, 145, 169, 133, 11, 12, 14, 13, 7, 6, 106, 103, 102, 105, 108, 109, 101,3, 2, 5, 8, 9, 1, 0, 22, 31, 4, 19,100, 145, 169, 133, 11, 12, 14, 13, 7, 6, 106, 103, 102, 105, 108, 109, 101]

# Shorter data for debugging
short = [3, 2,6,]


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
        ticks+=1
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


def mergeSort(list):
    return mergeSortRecursive(list, 0, len(list)-1)
    


def mergeSortRecursive(list, startIndex, endIndex):
    ticks = 0
    if startIndex == endIndex:
        return 1

    # If we get here, we have at list a separation of two
    centerIndex = math.floor((startIndex + endIndex)/2)

    # Do the recursion
    leftTicks = mergeSortRecursive(list, startIndex, centerIndex)
    rightTicks = mergeSortRecursive(list, centerIndex+1, endIndex)
    
    # Merge Results
    tempList = []
    firstIndex = startIndex
    secondIndex = centerIndex + 1

    # Merge in the lowest value
    # Stop when one side is done
    while firstIndex < centerIndex+1 and secondIndex < endIndex+1:
      ticks += 1
      firstValue = list[firstIndex]
      secondValue = list[secondIndex]
      if firstValue < secondValue :
        tempList.append(firstValue)
        firstIndex += 1
      else:
        tempList.append(secondValue)
        secondIndex += 1

    # Add the remaining values on the left (if any)
    while firstIndex < centerIndex+1:
      ticks += 1
      value = list[firstIndex]
      tempList.append(value)
      firstIndex += 1

    # Add the remaining values on the right (if any)
    while secondIndex < endIndex+1:
      ticks += 1
      value = list[secondIndex]
      tempList.append(value)
      secondIndex += 1

    # Put the value back into the list in sorted order
    tempIndex = 0
    for index in range(startIndex, endIndex+1):
      list[index] = tempList[tempIndex]
      tempIndex += 1

    return leftTicks + rightTicks + ticks



# Print the header for the table
print("Count BubbleSlow BubbleFast Selection Insertion Merge")

# Loop over every length of the list
# And print the ticks for each algorithm
for i in range(1, len(data)):
    tempList = data[:i]
    first = bubbleSortSlow(tempList.copy())
    second = bubbleSortFast(tempList.copy())
    third = selectionSort(tempList.copy())
    forth = insertionSort(tempList.copy())
    fifth = mergeSort(tempList.copy())
    print(f"{i} {first} {second} {third} {forth} {fifth}")
