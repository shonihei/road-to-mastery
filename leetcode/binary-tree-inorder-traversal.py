"""
Given a binary tree, return the inorder traversal of its nodes' values.
"""

class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

def inorderTraversal(root, iterative=True):
    lst = []
    if not iterative:
        _recursiveInorderTraversal(root, lst)
    else:
        _iterInorderTraversal(root, lst)
    return lst

def _recursiveInorderTraversal(root, lst):
    if root:
        _recursiveInorderTraversal(root.left, lst)
        lst.append(root.val)
        _recursiveInorderTraversal(root.right, lst)

def _iterInorderTraversal(root, lst):
    if root:
        stack = []

        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            lst.append(cur.val)
            cur = cur.right
            
