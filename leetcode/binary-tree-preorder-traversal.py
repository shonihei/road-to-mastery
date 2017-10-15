"""
Given a binary tree, return the preorder traversal of its nodes' values.
"""

class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

def preorderTraversal(root, iteratively=False):
    lst = []
    if iteratively:
        _iterativePreorderTraversal(root, lst)
    else:
        _recursivePreorderTraversal(root, lst)
    return lst

def _recursivePreorderTraversal(root, lst):
    if root:
        lst.append(root.val)
        _recursivePreorderTraversal(root.left, lst)
        _recursivePreorderTraversal(root.right, lst)
    
def _iterativePreorderTraversal(root, lst):
    if root:
        stack = [root]
        while stack:
            cur = stack.pop()
            lst.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
