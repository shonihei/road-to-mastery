"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""

class TreeNode(object):
	def __init__(self, x, left=None, right=None):
		self.val = x
		self.left = left
		self.right = right

def hasPathSum(root, sum):
	"""
	:type root: TreeNode
	:type sum: int
	:rtype: bool
	"""
	if not root:
		if sum == 0:
			return True
		return False
	elif root.left and root.right:
		return hasPathSum(root.left, sum - root.val) or hasPathSum(root.right, sum - root.val)
	elif root.left:
		return hasPathSum(root.left, sum - root.val)
	elif root.right:
		return hasPathSum(root.right, sum - root.val)
	elif not root.left and not root.right:
		if sum - root.val == 0:
			return True
		return False

t = TreeNode(5,TreeNode(4,TreeNode(11,TreeNode(7),TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))