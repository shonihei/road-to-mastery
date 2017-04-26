# task: given two linked lists, merge them in an alternating manner.

class Node:
    def __init__(self, v=None, n=None):
        self.key = v
        self.next = n

def merge(h1, h2):
    i = h1
    j = h2
    while i and j:
        temp = i.next
        i.next = j
        j = j.next
        i.next.next = temp
        i = temp
        h2 = j
    return h1, h2

A = Node(1, Node(2, Node(3)))
B = Node(4, Node(5, Node(6, Node(7, Node(8)))))
A, B = merge(A, B)
