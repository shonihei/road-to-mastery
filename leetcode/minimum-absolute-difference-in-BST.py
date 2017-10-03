"""
Given a binary search tree with non-negative values, find the minimum
absolute difference between values of any two nodes.
"""

import unittest

class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

def add(root, val):
    if not root:
        return TreeNode(val)
    else:
        if val < root.val:
            if root.left:
                add(root.left, val)
            else:
                root.left = TreeNode(val)
        else:
            if root.right:
                add(root.right, val)
            else:
                root.right = TreeNode(val)

def add_all(root, vals):
    if not root:
        root = TreeNode(vals.pop(0))
    for val in vals:
        add(root, val)
    return root

def getMinimumDifference(root):
    lst = flatten(root)
    diff = float('inf')
    for i in range(1, len(lst)):
        if lst[i] - lst[i - 1] < diff:
            diff = lst[i] - lst[i - 1]
    return diff

def flatten(root, lst=None):
    if lst is None:
        lst = []
    if root:
        if root.left:
            flatten(root.left, lst)
        lst.append(root.val)
        if root.right:
            flatten(root.right, lst)
        return lst

class Test(unittest.TestCase):
    def test1(self):
        root = add_all(None, [1, 3, 2])
        self.assertEqual(getMinimumDifference(root), 1)

if __name__ == "__main__":
    unittest.main()
