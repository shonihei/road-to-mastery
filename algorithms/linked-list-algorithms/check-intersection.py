# task: given two linked list, determine if they intersect at any point
#       intersection is defined by a node that is shared among two linked lists

class Node:
    def __init__(self, v=None, n=None):
        self.key = v
        self.next = n

# O(n) soln with O(n) spatial complexity
def check_intersection(l1, l2):
    d = dict()
    i = l1
    while i:
        d[id(i)] = True
        i = i.next
    j = l2
    while j:
        if id(j) in d:
            return True
        j = j.next
    return False

A = Node(5, Node(3, Node(8, Node(4))))
B = Node(7, A.next.next)
C = Node(5, Node(3, Node(8, Node(4))))
print(check_intersection(A, B))
print(check_intersection(A, C))
