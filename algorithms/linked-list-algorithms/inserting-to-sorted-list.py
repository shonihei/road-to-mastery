#task: given a sorted linked list, insert a new node so that the sorted order is retained

class Node:
    def __init__(self, v=None, n=None):
        self.key = v
        self.next = n

def insert(head, v):
    if not head:
        return Node(v)
    if not head.next:
        if v < head.key:
            return Node(v, head)
        else:
            head.next = Node(v)
            return head
    n = head
    while n.next and v > n.next.key:
        n = n.next
    new_node = Node(v, n.next)
    n.next = new_node
    return head

def p(head):
    s = ""
    while head:
        s += str(head.key) + " -> "
        head = head.next
    return s + "."

A = Node(1, Node(11, Node(13, Node(24, Node(29, Node(32, Node(35)))))))
print(p(A))
A = insert(A, 15)
print(p(A))
