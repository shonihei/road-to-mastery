# task: given a tree and two values that are represented in the tree, find the lowest common ancestor between the two elements and return its pointer

class Node:
    def __init__(self, v=None, l=None, r=None):
        self.key = v
        self.lc = l
        self.rc = r

def LCA(node, a, b):
    if not node:
        return None
    path_a = []
    path_b = []
    # path to a
    cur = node
    while cur:
        path_a.append(cur)
        if cur.key == a:
            break
        elif a < cur.key:
            cur = cur.lc
        else:
            cur = cur.rc
    else:
        raise Exception("{} is not in this tree".format(a))

    cur = node
    while cur:
        path_b.append(cur)
        if cur.key == b:
            break
        elif b < cur.key:
            cur = cur.lc
        else:
            cur = cur.rc
    else:
        raise Exception("{} is not in this tree".format(b))

    # reverse one path array and then find the first common occurence
    path_a.reverse()
    for i in path_b:
        if i in path_a:
            return i
    return None

def in_order(node, l=[]):
    if node:
        in_order(node.lc, l)
        l.append(node.key)
        in_order(node.rc, l)
    return l

A = Node(15, Node(10, Node(5), Node(12)), Node(24, Node(20), Node(27)))
a = LCA(A, 12, 27)
print("lowest common ancestor between 12 and 27 is {}".format(a.key))
