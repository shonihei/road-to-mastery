# task: implement an AVL Tree class

class Node:
    def __init__(self, v=None, p=None, l=None, r=None):
        self.key = v
        self.p = p
        self.lc = l
        self.rc = r
        self.bf = 0

def insert(h, v):
    if not h:
        return Node(v)
    elif h.key == v:
        return h
    elif v < h.key:
        if not h.lc:
            h.lc = Node(v, h)
            update_bf(h.lc)
            return h
        h.lc = insert(h.lc, v)
        return h
    else:
        if not h.rc:
            h.rc = Node(v, h)
            update_bf(h.rc)
            return h
        h.rc = insert(h.rc, v)
        return h
    
def update_bf(n):
    if n:
        if n.bf < -1 or n.bf > 1:
            print("rebalancing at {}".format(n.key))
            rebalance(n)
            return
        if n.p:
            if n == n.p.rc:
                n.p.bf += 1
            if n == n.p.lc:
                n.p.bf -= 1
            if n.p.bf != 0:
                update_bf(n.p)

A = insert(None, 20)
A = insert(A, 10)
A = insert(A, 25)
A = insert(A, 30)
A = insert(A, 35)
