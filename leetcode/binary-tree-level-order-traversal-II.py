"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""

class TreeNode(object):
	def __init__(self, x, left=None, right=None):
		self.val = x
		self.left = left
		self.right = right

def levelOrderBottom(root):
	"""
	:type root: TreeNode
	:rtype: List[List[int]]
	"""
	out = []
	_levelOrderBottom(out, root, 1)
	return out

def _levelOrderBottom(lst, root, level):
	if root:
		if level > len(lst):
			lst.insert(0, [root.val])
		else:
			lst[len(lst) - level].append(root.val)
		_levelOrderBottom(lst, root.left, level + 1)
		_levelOrderBottom(lst, root.right, level + 1)

tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
