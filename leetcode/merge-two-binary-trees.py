"""
Given two binary trees and imagine that when you put one of them to cover the other,
some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap,
then sum node values up as the new value of the merged node. Otherwise, the NOT null node will
be used as the node of new tree.
"""

class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

def mergeTrees(t1, t2):
    if not t1 and not t2:
        return None
    elif not t1 and t2:
        return t2
    elif t1 and not t2:
        return t1
    else:
        t1.val += t2.val
        t1.left = mergeTrees(t1.left, t2.left)
        t1.right = mergeTrees(t1.right, t2.right)
        return t1

def print_in_order(t1):
    if not t1:
        return
    if t1.left:
        print_in_order(t1.left)
    print(t1.val)
    if t1.right:
        print_in_order(t1.right)

t1 = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
t2 = TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3, None, TreeNode(7)))
t1 = mergeTrees(t1, t2)
