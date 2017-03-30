class Node:
    def __init__(self, item, children=None):
        self.key = item
        self.children = children

    def __repr__(self):
        return self.key

class Tree:
    def __init__(self, num_children):
        self.root = None
        self.size = 0

    def add(self, item):
        raise NotImplementedError("generic tree does not have insertion algorithm")

    def __contains__(self, item):
        """Search for item using BST"""
        if not self.root:
            return False
        queue = [self.root]
        while queue:
            current_node = queue.pop(0)
            if current_node.key == item:
                return True
            if current_node.children:
                for child in current_node.children:
                    queue.append(child)
        return False
