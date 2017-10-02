"""
Given a Binary Search Tree (BST), convert it to a Greater Tree such that 
every key of the original BST is changed to the original key plus sum of 
all keys greater than the original key in BST.
"""

import unittest

class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

def convertBST(root):
    return _convertBST(root)

total = 0

def _convertBST(root):
    if root:
        global total
        _convertBST(root.right)
        root.val += total
        total = root.val
        print(total)
        _convertBST(root.left)

root = TreeNode(5, TreeNode(2), TreeNode(13, TreeNode(10), TreeNode(20)))
convertBST(root)
