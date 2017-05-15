class Node:
    def __init__(self, v=None, l=None, r=None):
        self.key = v
        self.lc = l
        self.rc = r

def add(root, new_node):
    if root is None:
        root = new_node 
    else:
        if new_node.key < root.key:
            if not root.lc:
                root.lc = new_node
            else:
                add(root.lc, new_node)
        else:
            if not root.rc:
                root.rc = new_node
            else:
                add(root.rc, new_node)

def in_order(root):
    if root:
        in_order(root.lc)
        print(root.key)
        in_order(root.rc)
            
a = Node(10)
add(a, Node(8))
add(a, Node(2))
add(a, Node(23))
add(a, Node(54))
