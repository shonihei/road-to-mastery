# task: given a binary tree, swap all children

class Node:
    def __init__(self, v, l=None, r=None):
        self.key = v
        self.lc = l
        self.rc = r

def swap(tree):
    if not tree:
        return tree
    q = [tree]
    while q:
        cur_node = q.pop(0)
        cur_node.lc, cur_node.rc = cur_node.rc, cur_node.lc
        if cur_node.lc:
            q.append(cur_node.lc)
        if cur_node.rc:
            q.append(cur_node.rc)
    return tree

A = Node(10, Node(23, Node(34), Node(45)), Node(32, Node(40), Node(50)))
A = swap(A)

