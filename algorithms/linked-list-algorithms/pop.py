class Node:
    def __init__(self, v=None, n=None):
        self.key = v
        self.next = n

def pop(node):
    if not node:
        raise IndexError("cannot pop from empty list")
    node = node.next
    return node

a = Node("a", Node("b", Node("c")))
print(a.key)
a = pop(a)
print(a.key)
