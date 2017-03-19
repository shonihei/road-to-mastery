# Not complete => Implement In-order traversal

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def add(self, num):
        if not root:
            self.root = Node(num)
        else:
            self.addAux(self.root, num)

    def addAux(self, node, num):
        d = node.data
        if d == num:
            return
        elif num > d:

def check_binary_search_tree_(root):
    if not root:
        return True
    return check_left(root.left, root.data) and check_right(root.right, root.data)

def check_left(root, p):
    if not root:
        return True
    if root.data > p:
        return False
    return check_left(root.left, root.data) and check_right(root.right, root.data)

def check_right(root, p):
    if not root:
        return True
    if root.data < p:
        return False
    return check_left(root.left, root.data) and check_right(root.right, root.data)
