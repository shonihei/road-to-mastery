"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
"""

def lowestCommonAncestor(root, p, q):
    if root is None:
        return None
    else:
        if root.val == p.val or root.val == q.val:
            return root
        else:
            if root.val > p.val and root.val > q.val:
                return lowestCommonAncestor(root.left, p, q)
            elif root.val < p.val and root.val < q.val:
                return lowestCommonAncestor(root.right, p, q)
            else:
                return root