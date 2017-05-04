# task: given a doubly linked list, reverse it

class Node:
    def __init__(self, v=None, prev=None, next=None):
        self.key = v
        self.prev = prev
        self.next = next

def reverse(head):
    new_head = head
    while new_head.next:
        new_head = new_head.next
    node = new_head
    while True:
        node.next, node.prev = node.prev, node.next
        node = node.next
        if not node:
            break
    return new_head

A = Node(3)
B = Node(2)
C = Node(7)
A.next = B
B.prev = A
B.next = C
C.prev = B
head = reverse(A)
