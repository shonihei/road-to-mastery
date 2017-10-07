"""
Given a binary tree, check whether it is a mirror of
itself (ie, symmetric around its center).
"""

class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

def isSymmetric(root):
    if not root:
        return True
    return _isSymmetric(root.left, root.right)

def _isSymmetric(left, right):
    if not left and not right:
        return True
    if not left and right:
        return False
    if left and not right:
        return False
    if left.val != right.val:
        return False
    else:
        inner = _isSymmetric(right.left, left.right)
        outer = _isSymmetric(left.left, right.right)
        return inner and outer

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            t = TreeNode(1,
                TreeNode(2,
                    TreeNode(3),
                    TreeNode(4),
                ),
                TreeNode(2,
                    TreeNode(4),
                    TreeNode(3),
                )
            )
            self.assertTrue(isSymmetric(t))

        def test2(self):
            t = TreeNode(1,
                TreeNode(2,
                    None,
                    TreeNode(3)
                ),
                TreeNode(2,
                    None,
                    TreeNode(3),
                )
            )
            self.assertFalse(isSymmetric(t))

        def test3(self):
            t = TreeNode(1,
                TreeNode(2),
                TreeNode(3),
            )
            self.assertFalse(isSymmetric(t))

    unittest.main()