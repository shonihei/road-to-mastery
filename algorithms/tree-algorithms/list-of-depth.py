#task: given a binary tree, create a linked list at every depth of the tree

class Node:
    def __init__(self, v=None, l=None, r=None):
        self.key = v
        self.lc = l
        self.rc = r

def list_of_depths(tree):
    if not tree:
        return []
    output = []
    q = [tree]
    while q:
        temp = []
        t = q.pop()
        if t.lc:
            temp.append(t.lc)
        if t.rc:
            temp.append(t.rc)
        head = Node(t.key)
        n = head
        while q:
            t = q.pop()
            if t.lc:
                temp.append(t.lc)
            if t.rc:
                temp.append(t.rc)
            n.lc = Node(t.key)
            n = n.lc
        q = temp
        output.append(head)
    return output

tree = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))
A = list_of_depths(tree)
for head in A:
    s = ""
    while head:
        s += str(head.key) + " -> "
        head = head.lc
    s += "."
    print(s)
        
