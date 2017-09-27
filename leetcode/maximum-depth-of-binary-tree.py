"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node
 down to the farthest leaf node.
"""

import unittest

class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
    if not root:
        return 0
    else:
        left = 1 + maxDepth(root.left)
        right = 1 + maxDepth(root.right)
        return max(left, right)

class Test(unittest.TestCase):
    def test_1(self):
        tree = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, TreeNode(6, TreeNode(7))))
        self.assertEqual(maxDepth(tree), 4)

if __name__ == "__main__":
    unittest.main()
