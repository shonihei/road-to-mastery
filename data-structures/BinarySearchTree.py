class Node:
    def __init__(self, data, left=None, right=None):
        self.key = data
        self.left = left
        self.right = right

'''
Wrapper class for Binary Search Tree
'''
class BinarySearchTree:
    ###============CONSTRUCTOR=============###
    def __init__(self):
        self.root = None
        self.size = 0


    ###============REPR=============###
    def __repr__(self):
        '''
            prints the content of the tree in an inorder traversal
        '''
        s = self.repr_aux_inorder(self.root)
        return s + "."

    def repr_aux_inorder(self, r, s=""):
        if r:
            left = self.repr_aux_inorder(r.left, s)
            right = self.repr_aux_inorder(r.right, s)
            s += left + str(r.key) + " -> "+ right
        return s

    def repr_aux_preorder(self, r, s=""):
        if r:
            left = self.repr_aux_preorder(r.left, s)
            right = self.repr_aux_preorder(r.right, s)
            s += str(r.key) + " -> " + left + right
        return s

    def repr_aux_postorder(self, r, s=""):
        if r:
            left = self.repr_aux_postorder(r.left, s)
            right = self.repr_aux_postorder(r.right, s)
            s += left + right + str(r.key) + " -> "
        return s


    ###============ADD=============###
    def add(self, item):
        if isinstance(item, (float, int, str)):
            if not self.root:
                self.root = Node(item)
            else:
                self.add_aux(self.root, item)
            self.size += 1
        elif isinstance(item, (list, tuple)):
            for element in item:
                self.add(element)

    def add_aux(self, root, item):
        if item > root.key:
            if not root.right:
                root.right = Node(item)
                return
            self.add_aux(root.right, item)
        elif item < root.key:
            if not root.left:
                root.left = Node(item)
                return
            self.add_aux(root.left, item)
        return


    ###============SEARCH=============###
    def search(self, target):
        return self.search_aux(self.root, target)

    def search_aux(self, root, target):
        if not root:
            return False
        if root.key == target:
            return True
        else:
            if target > root.key:
                return self.search_aux(root.right, target)
            else:
                return self.search_aux(root.left, target)


    ###============DELETE=============###
    def find_minimum(self, root):
        """
        Return the node storing the minimum value in a subtree
        **Used as a helper function for deletion**
        """
        if not root.left:
            return root
        else:
            return self.find_minimum(root.left)

    def delete(self, target):
        if not self.root:
            return
        self.delete_aux(self.root, target)

    def delete_aux(self, root, target, parent=None):
        # In the case of an empty subtree, return none
        if not root:
            return
        # target is larger than current, explore right
        elif target > root.key:
            self.delete_aux(root.right, target, root)
        # target is smaller than current, explore left
        elif target < root.key:
            self.delete_aux(root.left, target, root)
        # we have found our target
        else:
            # case 1: no children
            if not root.left and not root.right:
                if parent.left == root:
                    parent.left = None
                    self.size -= 1
                    return
                else:
                    parent.right = None
                    self.size -= 1
                    return

            # case 2: one children
            # case 2.a: left child
            if root.left and not root.right:
                if parent.left == root:
                    parent.left = root.left
                    self.size -= 1
                    return
                else:
                    parent.right = root.left
                    self.size -= 1
                    return

            # case 2.b: right child
            if not root.left and root.right:
                if parent.left == root:
                    parent.left = root.right
                    self.size -= 1
                    return
                else:
                    parent.right = root.right
                    self.size -= 1
                    return

            # case 3: two children
            # find minimum in right subtree
            minimum_node = self.find_minimum(root.right)
            self.delete(minimum_node.key)
            root.key = minimum_node.key
            return


    ###============GET_HEIGHT=============###
    def get_height(self):
        return self.get_height_aux(self.root)

    def get_height_aux(self, root):
        if not root:
            return -1
        else:
            left = self.get_height_aux(root.left) + 1
            right = self.get_height_aux(root.right) + 1
            return max(left, right)


    ###============GET_NODE_COUNT=============###
    def get_node_count(self):
        # cheaty way would be to just return self.size...
        # but i'm a better person than that
        return self.get_node_count_aux(self.root)

    def get_node_count_aux(self, root, count=0):
        if root:
            left = self.get_node_count_aux(root.left)
            right = self.get_node_count_aux(root.right)
            count = 1 + left + right
        return count


    ###============GET_MIN=============###
    def get_min(self):
        if not self.root:
            raise IndexError("tree is empty")
        return self.get_min_aux(self.root)

    def get_min_aux(self, root):
        if not root.left:
            return root.key
        else:
            return self.get_min_aux(root.left)


    ###============GET_MAX=============###
    def get_max(self):
        if not self.root:
            raise IndexError("tree is empty")
        return self.get_max_aux(self.root)

    def get_max_aux(self, root):
        if not root.right:
            return root.key
        else:
            return self.get_max_aux(root.right)


    ###============IS_BINARY_SEARCH_TREE=============###
    def is_bst(self):
        if not self.root:
            return True
        return self.is_bst_aux(self.root)

    def is_bst_aux(self, root, min_val=None, max_val=None):
        if not root:
            return True
        if min_val is not None and root.key > min_val:
            return False
        if max_val is not None and root.key < max_val:
            return False
        return self.is_bst_aux(root.left, None, root.key) and self.is_bst_aux(root.right, root.key, None)


def main():
    t = BinarySearchTree()
    t.add([5, 3, 7, 1, 4, 6, 8, 0, 2, 9])
    print(t)
    t.delete(5)
    print(t)
    print(t.get_height())
    print(t.get_node_count())

if __name__ == "__main__":
    main()
