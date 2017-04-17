# task: given two linked list whose node contains a single digit, return a new linked list with the sum of
#       of the two lists.
# example:
#    input:    7 -> 1 -> 6 -> .
#              5 -> 9 -> 2 -> .
#    output:   2 -> 1 -> 9 -> .
#    this calculation signifies 617 + 295 = 912

class Node:
    def __init__(self, v=None, n=None):
        self.key = v
        self.next = n

def sum_list(l1, l2):
    i = l1
    j = l2
    out = None
    n = out
    carry = 0
    while i and j:
        s = i.key + j.key + carry
        if s > 9:
            carry = 1
        else:
            carry = 0
        digit = s % 10
        if not out:
            out = Node(digit)
            n = out
        else:
            n.next = Node(digit)
            n = n.next
        i = i.next
        j = j.next
    if i:
        n.next = i
    if j:
        n.next = j
    while n:
        s = n.key + carry
        if s > 9:
            carry = 1
        else:
            carry = 0
        n.key = s % 10
        n = n.next
    return out

A = Node(7, Node(1, Node(6, Node(3))))
B = Node(5, Node(9, Node(2)))
C = sum_list(A, B)
