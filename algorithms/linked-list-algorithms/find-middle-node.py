# task: given a singly linked list, find the middle element

class Node:
    def __init__(self, v=None, n=None):
        self.key = v
        self.next = n

def middle_node(n):
    # find the length
    c = 0
    t = n
    while t:
        c += 1
        t = t.next

    for i in range(c // 2):
        n = n.next
    return n.key

A = Node(3, Node(2, Node(5, Node(1, Node(10)))))
B = Node(3, Node(2, Node(5, Node(1, Node(10, Node(12))))))
print(middle_node(A))
print(middle_node(B))
