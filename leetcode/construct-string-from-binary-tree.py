"""
You need to construct a string consists of parenthesis and integers from a binary tree
with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()".
And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.
"""

import unittest

class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

def tree2str(t):
    if not t:
        return ""
    if not t.left and not t.right:
        return str(t.val)
    else:
        left = tree2str(t.left)
        right = tree2str(t.right)
        if left == "" and right != "":
            left = "()"
            right = "(" + right + ")"
        elif left != "" and right == "":
            left = "(" + left + ")"
            right = ""
        else:
            left = "(" + left + ")"
            right = "(" + right + ")"
        return str(t.val) + left + right

class Test(unittest.TestCase):
    def test1(self):
        root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
        self.assertEqual(tree2str(root), "1(2(4))(3)")
    
    def test2(self):
        root = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3))
        self.assertEqual(tree2str(root), "1(2()(4))(3)")

if __name__ == "__main__":
    unittest.main()
