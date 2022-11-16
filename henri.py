class Node:
    def __init__(self, name):
        self.name = name
        self.edges = []

count = 3

matrix = []

for x in range(count):
    matrix.append([])
    for y in range(count):
        n = Node("Hi")
        matrix[x][y] = n

for x in range(count):
    for y in range(count):
        n = matrix[x][y]
        if x > 0:
            n.edges.append(matrix[x-1][y])
