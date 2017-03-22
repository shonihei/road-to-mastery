# This is not a problem, just a practice in implementing BFS and DFS in an
# iterative approach as well as a recursive one.

class Node:
    def __init__(self, item, left=None, right=None):
        self.key = item
        self.left = left
        self.right = right

def BFS(root, target):
    numOp = 0
    if not root:
        return False, numOp
    queue = [root]
    while queue:
        cur_node = queue.pop(0)
        print("Checking {}".format(cur_node.key))

        numOp += 1
        if cur_node.key == target:
            return True, numOp

        if cur_node.left:
            queue.append(cur_node.left)
        if cur_node.right:
            queue.append(cur_node.right)
    return False, numOp

def DFS(root, target):
    numOp = 0
    if not root:
        return False, numOp
    stack = [root]
    while stack:
        cur_node = stack.pop()
        print("Checking {}".format(cur_node.key))

        # Comparison
        numOp += 1
        if cur_node.key == target:
            return True, numOp

        if cur_node.right:
            stack.append(cur_node.right)
        if cur_node.left:
            stack.append(cur_node.left)
    return False, numOp

def DFSrecursive(root, target):
    if not root:
        return False
    left = DFSrecursive(root.left, target)
    print("Checking {}".format(root.key))
    if root.key == target:
        return True
    right = DFSrecursive(root.right, target)
    return left or right

def main():
    root = Node(10, Node(5, Node(3), Node(7)), Node(13, Node(11), Node(17)))
    print("Searching for 13")
    print("BFS :")
    found, numOp = BFS(root, 13)
    if found:
        print("Found in {} operations".format(numOp))
    else:
        print("Not found")
    print()
    print("DFS :")
    found, numOp = DFS(root, 13)
    if found:
        print("Found in {} operations".format(numOp))
    else:
        print("Not found")
    print()
    print(DFSrecursive(root, 14))

if __name__ == "__main__":
    main()
