"""
Given a binary search tree and the lowest and highest boundaries as L and R,
trim the tree so that all its elements lies in [L, R] (R >= L). You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.
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
    elif val < root.val:
        if not root.left:
            root.left = TreeNode(val)
            return root
        else:
            root.left = add(root.left, val)
            return root
    else:
        if not root.right:
            root.right = TreeNode(val)
            return root
        else:
            root.right = add(root.right, val)
            return root

def add_all(root, vals):
    for val in vals:
        add(root, val)
    return root

def check_equal(root, other_root):
    if not root and not other_root:
        return True
    if root and not other_root:
        return False
    if not root and other_root:
        return False
    if root.val != other_root.val:
        return False
    else:
        left = check_equal(root.left, other_root.left)
        right = check_equal(root.right, other_root.right)
        return True if left and right else False

def trimBST(root, L, R):
    if not root:
        return root
    else:
        if root.val < L:
            root = trimBST(root.right, L, R)
            return root
        elif root.val > R:
            root = trimBST(root.left, L, R)
            return root
        else:
            root.left = trimBST(root.left, L, R)
            root.right = trimBST(root.right, L, R)
            return root

class Test(unittest.TestCase):
    def test1(self):
        root = TreeNode(3)
        add_all(root, [0, 4, 2, 1])
        trimBST(root, 1, 3)
        other_root = TreeNode(3, TreeNode(2, TreeNode(1)))
        self.assertTrue(check_equal(root, other_root))
    
    def test2(self):
        root = TreeNode(1, TreeNode(0), TreeNode(2))
        trimBST(root, 1, 2)
        other_root = TreeNode(1, None, TreeNode(2))
        self.assertTrue(check_equal(root, other_root))

    def test3(self):
        root = TreeNode(3, TreeNode(1), TreeNode(5))
        root = trimBST(root, 5, 6)
        other_root = TreeNode(5)
        self.assertTrue(check_equal(root, other_root))

if __name__ == "__main__":
    unittest.main()