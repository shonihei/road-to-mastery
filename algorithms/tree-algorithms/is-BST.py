# task: given a binary tree, write a function to check if the given tree is a valid binary search tree

class Node:
    def __init__(self, v=None, l=None, r=None):
        self.key = v
        self.lc = l
        self.rc = r

def is_BST(tree):
    if not tree:
        return True
    if not tree.lc and not tree.rc:
        return True
    # single child case
    if not tree.lc or not tree.rc:
        if tree.lc:
            if tree.lc.key > tree.key:
                return False
        else:
            if tree.rc.key < tree.key:
                return False
    else:
        if tree.lc.key > tree.key or tree.rc.key < tree.key:
            return False
    return is_BST(tree.lc) and is_BST(tree.rc)

A = Node(2, Node(1), Node(3))
B = Node(2, Node(3), Node(1))
C = Node(6, Node(5, Node(4, Node(3, Node(2, Node(1))))))
print(is_BST(A))
print(is_BST(B))
print(is_BST(C))
