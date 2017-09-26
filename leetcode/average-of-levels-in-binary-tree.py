"""
Given a non-empty binary tree, return the average value of the nodes
on each level in the form of an array.
"""

class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

def averageOfLevels(root):
    q = [(0, root)]
    d = dict()
    while q:
        level, node = q.pop(0)
        d.setdefault(level, []).append(node.val)
        if node.left:
            q.append((level + 1, node.left))
        if node.right:
            q.append((level + 1, node.right))
    out = []
    for key in sorted(d.keys()):
        out.append(sum(d[key]) / float(len(d[key])))
    return out

t1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(averageOfLevels(t1))
