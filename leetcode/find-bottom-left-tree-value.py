"""
Given a binary tree, find the leftmost value in the last row of the tree.
"""

import unittest

class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findBottomLeftValue(root):
    q = [(0, root)]
    d = dict()
    max_depth = 0
    while q:
        depth, cur = q.pop(0)
        d.setdefault(depth, []).append(cur.val)
        if depth > max_depth:
            max_depth = depth
        if cur.left:
            q.append((depth + 1, cur.left))
        if cur.right:
            q.append((depth + 1, cur.right))
    return d[max_depth][0]

class Test(unittest.TestCase):
    def test1(self):
        t = TreeNode(2, TreeNode(1), TreeNode(3))
        self.assertEqual(findBottomLeftValue(t), 1)
    
    def test2(self):
        t = TreeNode(1,
            TreeNode(2,
                TreeNode(4)
            ),
            TreeNode(3,
                TreeNode(5,
                    TreeNode(7)
                ),
                TreeNode(6)
            )
        )
        self.assertEqual(findBottomLeftValue(t), 7)

if __name__ == "__main__":
    unittest.main()
