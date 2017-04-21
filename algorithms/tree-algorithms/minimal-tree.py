# task: given a sorted array with unique integer elements, write an algorithm to create
#       a BST with minimal height

class Node:
    def __init__(self, v=None, l=None, r=None):
        self.key = v
        self.lc = l
        self.rc = r

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, v):
        if not self.root:
            self.root = Node(v)
        else:
            self.insert_aux(self.root, v)

    def insert_aux(self, n, v):
        if v < n.key:
            if not n.lc:
                n.lc = Node(v)
            else:
                self.insert_aux(n.lc, v)
        else:
            if not n.rc:
                n.rc = Node(v)
            else:
                self.insert_aux(n.rc, v)

    def get_height(self):
        return self.get_height_aux(self.root)

    def get_height_aux(self, n):
        if not n:
            return -1
        else:
            return max(self.get_height_aux(n.lc), self.get_height_aux(n.rc)) + 1

    def print_by_level(self):
        if not self.root:
            print("empty")
        q = [self.root]
        while q:
            c = q.pop(0)
            print(c.key)
            if c.lc:
                q.append(c.lc)
            if c.rc:
                q.append(c.rc)
        
def minimal_tree(lst):
    return minimal_tree_aux(None, lst)

def minimal_tree_aux(tree, lst):
    if lst:
        mid = len(lst) // 2
        if not tree:
            tree = Tree()
            tree.insert(lst[mid])
        else:
            tree.insert(lst[mid])
        minimal_tree_aux(tree, lst[:mid])
        minimal_tree_aux(tree, lst[mid+1:])
        return tree

a = [1, 2, 3, 4, 5, 6, 7]
A = minimal_tree(a)
print("height is {}".format(A.get_height))
