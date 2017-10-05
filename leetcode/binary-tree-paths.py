"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:
"""

class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

def binaryTreePaths(root, lst=None):
    if lst is None:
        lst = []
    if root:
        
        
