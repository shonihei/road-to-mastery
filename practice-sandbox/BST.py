# task: just implement a Binary Search Tree using node class

class Node:
    def __init__(self, v=None, l=None, r=None):
        self.key = v
        self.lc = l
        self.rc = r

def insert(head, v):
    if not head:
        return Node(v)
    if v < head.key:
        head.lc = insert(head.lc, v)
    elif v > head.key:
        head.rc = insert(head.rc, v)
    return head

def delete(head, v):
    if not head:
        return head
    if v < head.key:
        head.lc = delete(head.lc, v)
    elif v > head.key:
        head.rc = delete(head.rc, v)
    else:
        # no children
        if not head.lc and not head.rc:
            return None
        # one child
        if head.lc and not head.rc:
            return head.lc
        if not head.lc and head.rc:
            return head.rc
        # two children
        else:
            i = head
            j = i.rc
            while j.lc:
                i = j
                j = j.lc
            head.key = j.key
            i.lc = None
            return head
    return head

def in_order(head, v=[]):
    if head:
        in_order(head.lc, v)
        v.append(head.key)
        in_order(head.rc, v)
    return v

def pre_order(head, v=[]):
    if head:
        v.append(head.key)
        pre_order(head.lc, v)
        pre_order(head.rc, v)
    return v

def post_order(head, v=[]):
    if head:
        post_order(head.lc, v)
        post_order(head.rc, v)
        v.append(head.key)
    return v

def find(head, v):
    if not head:
        return False
    if head.key == v:
        return True
    if head.key < v:
        return find(head.rc, v)
    else:
        return find(head.lc, v)

def get_height(head):
    if not head:
        return -1
    return max(get_height(head.lc), get_height(head.rc)) + 1

def LCA(head, a, b):
    if not head:
        return None
    path_to_a = []
    i = head
    while i:
        path_to_a.append(i)
        if i.key == a:
            break
        elif a < i.key:
            i = i.lc
        else:
            i = i.rc

    path_to_b =[]
    i = head
    while i:
        path_to_b.append(i)
        if i.key == b:
            break
        elif b < i.key:
            i = i.lc
        else:
            i = i.rc
    path_to_a.reverse()
    path_to_b.reverse()
    for i in path_to_a:
        if i in path_to_b:
            return i
    return None
    

A = insert(None, 10)
A = insert(A, 3)
A = insert(A, 20)
A = insert(A, 12)
A = insert(A, 22)
A = insert(A, 21)
