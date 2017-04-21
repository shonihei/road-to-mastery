# task: given a pointer to a node in a binary search tree, write an algorithm to return the node containing the
#       next largest element

class Node:
    def __init__(self, key=None, left_child=None, right_child=None, parent=None):
        self.k = key
        self.lc = left_child
        self.rc = right_child
        self.p = parent
        
def get_successor(node):
    if not node.p:
        n = node.rc
        while n.lc:
            n = n.lc
        return n
    no_children = not node.lc and not node.rc
    lc_of_parent = node == node.p.lc
    rc_of_parent = node == node.p.rc

    if node.lc or (no_children and lc_of_parent):
        return node.p
    if no_children and rc_of_parent:
        n = node.parent
        if not n.parent:
            return None
        return n.parent
    n = node.rc
    while n.lc:
        n = n.lc
    return n

A = Node(5)
B = Node(3)
C = Node(7)
A.lc = B
B.p = A
A.rc = C
C.p = A
print(get_successor(B).k)
