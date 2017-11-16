"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
"""

class TreeNode(object):
	def __init__(self, x, left=None, right=None):
		self.val = x
		self.left = left
		self.right = right

def isSubtree(s, t):
	"""
	:type s: TreeNode
	:type t: TreeNode
	:rtype: bool
	"""
	if isMatch(s, t): return True
	if not s: return False
	return isSubtree(s.left, t) or isSubtree(s.right, t)

def isMatch(s, t):
	if not(s and t):
		return s is t
	return (s.val == t.val and 
		isMatch(s.left, t.left) and 
		isMatch(s.right, t.right))

if __name__ == "__main__":
	import unittest

	class Test(unittest.TestCase):
		def test1(self):
			s = None
			t = None
			self.assertTrue(isSubtree(s, t))

		def test2(self):
			s = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
			t = TreeNode(4, TreeNode(1), TreeNode(2))
			self.assertTrue(isSubtree(s, t))
	
		def test3(self):
			s = TreeNode(3, TreeNode(4, TreeNode(1, TreeNode(0)), TreeNode(2)), TreeNode(5))
			t = TreeNode(4, TreeNode(1), TreeNode(2))
			self.assertFalse(isSubtree(s, t))
	
	unittest.main()