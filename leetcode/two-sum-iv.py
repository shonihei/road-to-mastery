"""
Given a Binary Search Tree and a target number, return true if there exist two elements in 
the BST such that their sum is equal to the given target.
"""

import unittest

class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def add(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = add(root.left, val)
        return root
    elif root.val < val:
        root.right = add(root.right, val)
        return root

def add_all(root, lst):
    for n in lst:
        add(root, n)

# assumption: all values in the BST is unique
def findTarget(root, k):
    d = dict()
    q = [root]
    while q:
        cur = q.pop(0)
        d[cur.val] = True
        if cur.left:
            q.append(cur.left)
        if cur.right:
            q.append(cur.right)
    for key in d:
        complement = k - key
        if complement != key and complement in d:
            return True
    return False

class Test(unittest.TestCase):
    def test1(self):
        t1 = TreeNode(5)
        add_all(t1, [3, 6, 2, 4, 7])
        self.assertEqual(findTarget(t1, 9), True)
    
    def test2(self):
        t1 = TreeNode(5)
        add_all(t1, [3, 6, 2, 4, 7])
        self.assertEqual(findTarget(t1, 28), False)

if __name__ == "__main__":
    unittest.main()
