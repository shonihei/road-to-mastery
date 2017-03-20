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
    numOp = 0
    return DFSrecursiveAux(root, target, numOp)

def DFSrecursiveAux(root, target, numOp):
    if root:
        DFSrecursiveAux(root.left, target, numOp + 1)
        if root.key == target:
            print("Found {} in {} moves".format(target, numOp))
        DFSrecursiveAux(root.right, target, numOp + 1)

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
    print(DFSrecursive(root, 17))

if __name__ == "__main__":
    main()
