contacts = [
    "Alfa",
    "Alfa",
    "Bravo",
    "Charlie",
    "Delta",
    "Echo",
    "Foxtrot",
    "Golf",
    "Hotel",
    "India",
    "Juliett",
    "Kilo",
    "Lima",
    "Mike",
    "November",
    "Oscar",
    "Papa",
    "Quebec",
    "Romeo",
    "Sierra",
    "Tango",
    "Uniform",
    "Victor",
    "Whiskey",
    "X-ray",
    "Yankee",
    "Zulu",
    "Zulu"
]


def findDuplicates1(list):
    ticks = 0
    for i in range(0, len(list)):
        for j in range(0, len(list)):
            ticks += 1
            if list[i] is list[j]:
                # print("Duplicate at index " + str(i) + " and " + str(j))
                pass
    return ticks

def findDuplicates2(list):
    ticks = 0
    for i in range(0, len(list)):
        for j in range(0, len(list)):
            if i == j:
                continue
            ticks += 1
            if list[i] is list[j]:
                # print("Duplicate at index " + str(i) + " and " + str(j))
                pass
    return ticks

def findDuplicates3(list):
    ticks = 0
    for i in range(0, len(list)):
        for j in range(i+1, len(list)):
            if i == j:
                continue
            ticks += 1
            if list[i] is list[j]:
                # print("Duplicate at index " + str(i) + " and " + str(j))
                pass
    return ticks

def findDuplicatesSorted(list):
  ticks = 0
  for i in range(0, len(list)-1):
    ticks += 1
    if list[i] is list[i+1]:
      pass #print("Found a duplicate at index " + str(i))
  return ticks


print("Contacts First_Method Second_Method Third_Method Sorted_Method")
for i in range(1, len(contacts)):
    first = findDuplicates1(contacts[0:i+1])
    second = findDuplicates2(contacts[0:i+1])
    third = findDuplicates3(contacts[0:i+1])
    sorted = findDuplicatesSorted(contacts[0:i+1])
    print(f"{i} {first} {second} {third} {sorted}")
