# task: given a linked list, perform a pair-wise swap

class Node:
    def __init__(self, v=None, n=None):
        self.key = v
        self.next = n

def pair_wise_swap(head):
    if not head or not head.next:
        return head
    i = head
    j = head.next
    while j:
        i.key, j.key = j.key, i.key
        i = j.next
        if not i:
            break
        j = i.next
    return head

def p(head):
    s = ""
    while head:
        s += str(head.key) + " -> "
        head = head.next
    return s + "."

A = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7)))))))
print(p(A))
A = pair_wise_swap(A)
print(p(A))
