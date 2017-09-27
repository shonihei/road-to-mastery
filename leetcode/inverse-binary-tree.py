"""
Invert a binary tree
"""
import unittest

class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flatten(root):
    out = []
    q = [root]
    while q:
        cur = q.pop(0)
        out.append(cur.val)
        if cur.left:
            q.append(cur.left)
        if cur.right:
            q.append(cur.right)
    return out

def invertTree(root):
    if root:
        root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root

class Test(unittest.TestCase):
    def test_1(self):
        t1 = TreeNode(
            4,
            TreeNode(
                2,
                TreeNode(1),
                TreeNode(3)
            ),
            TreeNode(
                7,
                TreeNode(6),
                TreeNode(9)
            )
        )
        t2 = TreeNode(
            4,
            TreeNode(
                7,
                TreeNode(9),
                TreeNode(6)
            ),
            TreeNode(
                2,
                TreeNode(3),
                TreeNode(1)
            ),
        )
        self.assertEqual(flatten(t2), flatten(invertTree(t1)))

if __name__ == "__main__":
    unittest.main()
