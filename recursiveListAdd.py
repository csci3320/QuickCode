class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class List:
    def __init__(self):
        self.root = None
        
    def add(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        current = self.root
        while current.next is not None:
            current = current.next
        current.next = Node(value)

    def add2(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        self.root = self.addRecursive(self.root, value)

    def addRecursive(self, node, value):
        if node is None:
            return Node(value)
        node.next = self.addRecursive(self, node.next, value)
        
