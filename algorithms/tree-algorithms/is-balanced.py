class TreeNode:
    def __init__(self, v=None, l=None, r=None):
        self.key = v
        self.lc = l
        self.rc = r

def get_height(tree):
    if not tree:
        return -1
    if not tree.lc and not tree.rc:
        return 0
    return 1 + max(get_height(tree.lc), get_height(tree.rc))

def is_balanced(tree):
    if not tree or not tree.lc and not tree.rc:
        return True
    l = get_height(tree.lc)
    r = get_height(tree.rc)
    if is_balanced(tree.lc) and is_balanced(tree.rc) and abs(l - r) <= 1:
        return True
    return False
    
A = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, TreeNode(6), TreeNode(7, TreeNode(10, TreeNode(100)))))
B = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5))
print(is_balanced(A))
print(is_balanced(B))
