#task: given a pointer to some node that has a valid next node, delete itself from the linkedlist without
#      an access to previous nodes.

# e.g) a -> b -> c -> d -> .
#      you are given a pointer to node 'c', but no other previous elements
#      turn the linked list into
#      a -> b -> d -> .

class Node:
    def __init__(self, v=None, n=None):
        self.key = v
        self.next = n

def delete_middle(node):
    if not node.next:
        raise Exception("faulty input")
    node.key = node.next.key
    node.next = node.next.next

def print_ll(head):
    s = ""
    while head:
        s += str(head.key) + " -> "
        head = head.next
    return s + "."

A = Node("A", Node("B", Node("C", Node("D"))))
pointer = A.next.next
print(print_ll(A))
delete_middle(pointer)
print(print_ll(A))
