"""
Print a binary tree in an m*n 2D string array following these rules:

The row number m should be equal to the height of the given binary tree.

The column number n should always be an odd number.

The root node's value (in string format) should be put in the exactly
middle of the first row it can be put. The column and the row where the
root node belongs will separate the rest space into two parts (left-bottom
part and right-bottom part). You should print the left subtree in the left-bottom
part and print the right subtree in the right-bottom part. The left-bottom part and
the right-bottom part should have the same size. Even if one subtree is none while the
other is not, you don't need to print anything for the none subtree but still need to
leave the space as large as that for the other subtree. However, if two subtrees are none,
then you don't need to leave space for both of them.

Each unused space should contain an empty string "".

Print the subtrees following the same rules.
"""

class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

def getHeight(root):
    if not root:
        return 0
    else:
        left = getHeight(root.left) + 1
        right = getHeight(root.right) + 1
        return max(left, right)

def printTree(root):
    if not root:
        return []
    height = getHeight(root)
    matrix = [["" for _ in range((2 ** height) - 1)] for __ in range(height)]
    _printTree(root, 0, 0, len(matrix[0]) - 1, matrix)
    return matrix

def _printTree(cur, depth, l, r, matrix):
    if not cur:
        return
    else:
        mid = (l + r) // 2
        matrix[depth][mid] = str(cur.val)
        _printTree(cur.left, depth + 1, l, mid - 1, matrix)
        _printTree(cur.right, depth + 1, mid + 1, r, matrix)

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            root = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3))
            out = [
                ["", "", "", "1", "", "", ""],
                ["", "2", "", "", "", "3", ""],
                ["", "", "4", "", "", "", ""]
            ]
            self.assertEqual(printTree(root), out)

    unittest.main()
