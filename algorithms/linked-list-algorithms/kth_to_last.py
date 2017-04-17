# task: given a linked list, find the kth to last node and return its key

class Node:
    def __init__(self, v=None, n=None):
        self.key = v
        self.next = n

def kth_from_last(head, k):
    # get length
    l = 0
    p = head
    while p:
        l += 1
        p = p.next
    if k > l - 1:
        raise IndexError("k is larger than list")
    p = head
    for i in range(l - k):
        p = p.next
    return p.key

A = Node(10, Node(7, Node(2, Node(4, Node(8)))))
print(kth_from_last(A, 4))
