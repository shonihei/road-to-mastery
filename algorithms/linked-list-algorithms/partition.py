# task: given a linked list and partition value x, split the linked list
#       such that any value less than x appears on the left of x and
#       any value more than or equal to x appears on the right

class Node:
    def __init__(self, v=None, n=None):
        self.key = v
        self.next = n

def partition(head, x):
    if not head:
        return None
    lt = None
    gte = None
    cur_node = head
    while cur_node:
        if cur_node.key < x:
            if not lt:
                lt = cur_node
                cur_node = cur_node.next
                lt.next = None
            else:
                tmp = cur_node
                cur_node = cur_node.next
                tmp.next = lt
                lt = tmp
        else:
            if not gte:
                gte = cur_node
                cur_node = cur_node.next
                gte.next = None
            else:
                tmp = cur_node
                cur_node = cur_node.next
                tmp.next = gte
                gte = tmp
    p = lt
    while p:
        if not p.next:
            p.next = gte
            break
        p = p.next
    head = lt
    return head

A = Node(7, Node(3, Node(4, Node(8, Node(1)))))
B = partition(A, 5)
