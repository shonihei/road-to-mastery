"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

class TreeNode(object):
	def __init__(self, x, left=None, right=None):
		self.val = x
		self.left = left
		self.right = right

def levelOrder(root):
	"""
	:type root: TreeNode
	:rtype: List[List[int]]
	"""
	lst = []
	_levelOrder(lst, root, 1)
	return lst

def _levelOrder(lst, root, level):
	if root:
		if level > len(lst):
			lst.append([root.val])
		else:
			lst[level - 1].append(root.val)
		_levelOrder(lst, root.left, level + 1)
		_levelOrder(lst, root.right, level + 1)

tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))