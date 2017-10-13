"""
You need to find the largest value in each row of a binary tree.
"""

class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

def largestValues(root):
    if not root:
        return []
    lst = []
    _largestValues(root, 0, lst)
    return lst
    
def _largestValues(root, depth, lst):
    if not root:
        return
    else:
        if depth >= len(lst):
            lst.append(root.val)
        elif lst[depth] < root.val:
            lst[depth] = root.val
        if root.left:
            _largestValues(root.left, depth + 1, lst)
        if root.right:
            _largestValues(root.right, depth + 1, lst)

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            root = TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9)))
            self.assertEqual(largestValues(root), [1, 3, 9])

    unittest.main()
