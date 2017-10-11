"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
"""

class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.left = left
        self.right = right

def sortedArraytoBST(nums):
    root = _sortedArraytoBST(nums, 0, len(nums) - 1, None)

def _sortedArraytoBST(nums, left, right, root):
    if left < right:
        mid = (left + right) // 2
        if not root:
            root = TreeNode(mid)
    return root