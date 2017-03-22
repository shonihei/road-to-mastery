# Fix Deletion!!!!

class Node:
    def __init__(self, data, left=None, right=None):
        self.key = data
        self.left = left
        self.right = right

'''
Wrapper class for Binary Search Tree
'''
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __repr__(self):
        '''
            prints the content of the tree in an inorder traversal
        '''
        lst = self.repr_aux(self.root)
        s = ""
        for item in lst:
            s += "{} -> ".format(item)
        return s + "."

    def repr_aux(self, r, lst=[]):
        if r:
            self.repr_aux(r.left)
            lst.append(r.key)
            self.repr_aux(r.right)
        return lst

    def add(self, item):
        if not self.root:
            self.root = Node(item)
        else:
            self.add_aux(self.root, item)
        self.size += 1

    def add_aux(self, root, item):
        if item > root.key:
            if not root.right:
                root.right = Node(item)
                return
            self.add_aux(root.right, item)
        elif item < root.key:
            if not root.left:
                root.left = Node(item)
                return
            self.add_aux(root.left, item)
        return

    def search(self, target):
        return self.search_aux(self.root, target)

    def search_aux(self, root, target):
        if not root:
            return False
        if root.key == target:
            return True
        else:
            if target > root.key:
                return self.search_aux(root.right, target)
            else:
                return self.search_aux(root.left, target)

    def delete(self, item):
        if not self.root:
            return
        else:
            self.delete_aux(self.root, item)

    def delete_aux(self, root, item):
        if not root:
            return
        else:
            if root.key == item:
                if not root.left and not root.right:
                    root = None
                    return
                if root.left and not root.right:
                    root = root.left
                    return
                if not root.left and root.right:
                    root = root.right
                    return
                else:
                    p = root.right
                    while p.left:
                        r = p
                        p = p.left
                    root.key = p.key
                    if p == r:
                        root.right = p.right
                    else:
                        r.left = None
                    return
            if root.left and root.left.key == item:
                p = root.left
                if not p.left and not p.right:
                    root.left = None
                    return
                if p.left and not p.right:
                    root.left = p.left
                    return
                if not p.left and p.right:
                    root.right = p.right
                    return
                else:
                    q = p.left
                    r = p
                    while q.right:
                        r = q
                        q = q.right
                    p.key = q.key
                    r.right = None
                    return
            if root.right and root.right.key == item:
                p = root.right
                if not p.left and not p.right:
                    root.right = None
                    return
                if p.left and not p.right:
                    root.left = p.left
                    return
                if not p.left and p.right:
                    root.right = p.right
                    return
                else:
                    q = p.right
                    r = p
                    while q.left:
                        r = q
                        q = q.left
                    p.key = q.key
                    r.left = None
                    return
            elif item < root.key:
                self.delete_aux(root.left, item)
            else:
                self.delete_aux(root.right, item)

def main():
    t = BinarySearchTree()
    for i in range(3, 25, 4):
        t.add(i)
    print(t)
    print(t.search(42))
    print(t.search(23))

if __name__ == "__main__":
    main()
