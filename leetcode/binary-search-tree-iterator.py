"""
Implement an iterator over a binary search tree (BST). Your iterator will be
initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory,
where h is the height of the tree.
"""

class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

def add(num, root=None):
    if not root:
        return TreeNode(num)
    else:
        if num < root.val:
            if not root.left:
                root.left = TreeNode(num)
            else:
                root.left = add(num, root.left)
            return root
        else:
            if not root.right:
                root.right = TreeNode(num)
            else:
                root.right = add(num, root.right)
            return root

def add_all(nums, root=None):
    starting_index = 0
    if root is None:
        root = TreeNode(nums[starting_index])
        starting_index += 1
    while starting_index < len(nums):
        add(nums[starting_index], root)
        starting_index += 1
    return root

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        if root is not None:
            self.stack.append(root)
            top = root
            while top.left:
                self.stack.append(top.left)
                top = top.left
            print()

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.stack else False

    def next(self):
        """
        :rtype: int
        """
        if not self.hasNext():
            raise StopIteration
        else:
            top = self.stack.pop()
            if top.right:
                self.stack.append(top.right)
                cur = top.right.left
                while cur:
                    self.stack.append(cur)
                    cur = cur.left
            return top.val                

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            lst = [4, 5, 3, 9, 10, 14]
            a = add_all(lst)
            i = BSTIterator(a)
            out = []
            while i.hasNext():
                out.append(i.next())
            lst.sort()
            self.assertEqual(lst, out)

    unittest.main()