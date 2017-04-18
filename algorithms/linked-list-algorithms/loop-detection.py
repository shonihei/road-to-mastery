# task: given a linked list, determine if the linked list has a loop or not.
#       loop is defined by its reference and not by its value

class Node:
    def __init__(self, v=None, n=None):
        self.key = v
        self.next = n

def detect_loop(l1):
    if not l1:
        return False
    i = l1
    d = dict()
    while i:
        if id(i) in d:
            return True
        else:
            d[id(i)] = True
            i = i.next
    return False

A = Node(7, Node(6, Node(5, Node(4))))
B = Node(7, Node(6, Node(5)))
print(detect_loop(A))
i = B
while i:
    if not i.next:
        break
    i = i.next
i.next = A
j = A
while j:
    if not j.next:
        break
    j = j.next
j.next = B
print(detect_loop(A))
    
