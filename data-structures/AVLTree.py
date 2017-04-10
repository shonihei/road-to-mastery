class Node:
    def __init__(self, val=None, p=None, l=None, r=None):
        self.key = val
        self.parent = p
        self.left_child = l
        self.right_child = r
        self.balance_factor = 0

    def __repr__(self):
        s = str(self.key)
        if self.is_root():
            return s + " root"
        return s

    def is_leaf(self):
        return not self.left_child and not self.right_child

    def is_root(self):
        return not self.parent

    def is_balanced(self):
        return self.balance_factor == 0

class AVLTree:
    """
    Self-balancing tree implemented using python
    rotation algorithms were implemented based on wikipedia
    """
    
    def __init__(self):
        """
        Constructor for AVLTree
        """
        self.root = None
        self.count = 0

    def __repr__(self):
        """
        Return string representation of the tree
        """
        l = self.inorder(self.root)
        s = ""
        for item in l:
            s += "Key : {}, BF : {}\n".format(item[0], item[1])
        return s

    def inorder(self, node, l=None):
        """
        Flatten the tree using inorder traversal
        """
        if l is None:
            l = []
        if node:
            self.inorder(node.left_child, l)
            l.append((node.key, node.balance_factor))
            self.inorder(node.right_child, l)
        return l

    def contains(self, v):
        """
        Search for v and return True if found, False otherwise
        """
        if not self.root:
            return False
        else:
            return self.contains_aux(self.root, v)

    def contains_aux(self, node, v):
        """
        Helper function for contains method
        """
        if not node:
            return False
        elif node.key == v:
            return True
        elif v < node.key:
            return self.contains_aux(node.left_child, v)
        else:
            return self.contains_aux(node.right_child, v)
    
    def insert(self, v):
        """
        Insert a new value to the tree
        """
        # tree is empty
        if not self.root:
            self.root = Node(v)
            print("{} now root".format(self.root.key))
        # tree is not empty
        else:
            # insert new node and retrieve the pointer to the newly created node
            new_node = self.insert_aux(self.root, v)
            if new_node:
                print("{} insertion successful!".format(new_node.key))
                # readjust the balance factor and rebalance if needed
                self.update_balance_factor(new_node)
            else:
                print("something went wrong...")

    def insert_aux(self, node, v):
        """
        Helper function to insert a new node recursively
        """
        if v < node.key:
            if not node.left_child:
                n = Node(v, node)
                node.left_child = n
                # return pointer to the new node
                return n
            return self.insert_aux(node.left_child, v)
        else:
            if not node.right_child:
                n = Node(v, node)
                node.right_child = n
                # return pointer to the new node
                return n
            return self.insert_aux(node.right_child, v)

    def update_balance_factor(self, node):
        """
        Recursively traverse up to the root and update the balance factor
        If balance factor is < -1 or > 1, rebalancing is neeeded
        """
        if node:
            # rebalance
            if node.balance_factor < -1 or node.balance_factor > 1:
                print("rebalancing at {}...".format(node.key))
                self.rebalance(node)
                return
            if node.parent:
                if node == node.parent.right_child:
                    node.parent.balance_factor += 1
                if node == node.parent.left_child:
                    node.parent.balance_factor -= 1
                # current node's parent is unbalanced, might have
                # screwed up the balance above, go to the parent and check
                if node.parent.balance_factor != 0:
                    self.update_balance_factor(node.parent)

    def rebalance(self, node):
        """
        Rebalance the tree by rotating the subtree about 'node'
        if right heavy: rotate left or rotate right then left
        if left heavy: rotate right or rotate left then right
        """
        # pointer to parent, used later to reassign parent
        cur_node_parent = node.parent
        root = not cur_node_parent

        # right heavy
        if node.balance_factor == 2:
            # zig-zag, must first rotate right
            if node.right_child.balance_factor == -1:
                new_node = self.rotate_right_left(node, node.right_child)
                if root:
                    self.root = new_node
                    new_node.parent = None
                else:
                    # reassign parent pointers
                    new_node.parent = cur_node_parent
                    cur_node_parent.right_child = new_node
                return
            # zig-zig, just rotate to left
            new_node = self.rotate_left(node, node.right_child)
            if root:
                self.root = new_node
                new_node.parent = None
            else:
                # reasssign parent pointers
                new_node.parent = cur_node_parent
                cur_node_parent.right_child = new_node
        else:
            # zig-zag, must first rotate left
            if node.left_child.balance_factor == 1:
                new_node = self.rotate_left_right(node, node.left_child)
                if root:
                    self.root = new_node
                    new_node.parent = None
                else:
                    # reassign parent pointers
                    new_node.parent = cur_node_parent
                    cur_node_parent.left_child = new_node
                return
            # zig-zig, just rotate to right
            new_node = self.rotate_right(node, node.left_child)
            if root:
                self.root = new_node
                new_node.parent = None
            else:
                # reassign parent pointers
                new_node.parent = cur_node_parent
                cur_node_parent.left_child = new_node

    def rotate_left(self, x, z):
        """
        Rotate subtree about node x
        x is the original parent of z
        after rotation, z is the parent of x
        """
        # x := parent of z
        # z := right child of z
        # y := left child of z
        y = z.left_child
        x.right_child = y
        if y:
            y.parent = x

        z.left_child = x
        x.parent = z

        if z.balance_factor == 0:
            x.balance_factor = 1
            z.balance_factor = -1
        else:
            x.balance_factor = 0
            z.balance_factor = 0
        return z

    def rotate_right(self, x, z):
        """
        Rotate the subtree about node x
        x is the original parent of z
        after rotation z is the parent of x
        """
        # x := parent of z
        # z := left child of z
        # y := right child of z
        y = z.right_child
        x.left_child = y
        if y:
            y.parent = x

        z.right_child = x
        x.parent = z

        if z.balance_factor == 0:
            x.balance_factor = -1
            z.balance_factor = 1
        else:
            x.balance_factor = 0
            z.balance_factor = 0
        return z

    def rotate_right_left(self, x, z):
        """
        Rotate right first about z and then rotate left about x
        x is the original parent of z
        after rotation y (z's left child) is the parent of both
        x and z
        """
        y = z.left_child
        t3 = y.right_child
        z.left_child = t3
        if t3:
            t3.parent = z
        y.right_child = z
        z.parent = y
        t2 = y.left_child
        x.right_child = t2
        if t2:
            t2.parent = x
        y.left_child = x
        x.parent = y

        if y.balance_factor > 0:
            x.balance_factor = -1
            z.balance_factor = 0
        elif y.balance_factor == 0:
            x.balance_factor = 0
            z.balance_factor = 0
        else:
            x.balance_factor = 0
            z.balance_factor = 1
        y.balance_factor = 0
        return y

    def rotate_left_right(self, x, z):
        """
        Rotate left first about z and then rotate right about x
        x is the original parent of z
        after rotation y (z's right child) is the parent of both
        x and z
        """
        y = z.right_child
        t3 = y.left_child
        z.right_child = t3
        if t3:
            t3.parent = z
        y.left_child = z
        z.parent = y
        t2 = y.right_child
        x.left_child = t2
        if t2:
            t2.parent = x
        y.right_child = x
        x.parent = y

        if y.balance_factor < 0:
            x.balance_factor = 1
            z.balance_factor = 0
        elif y.balance_factor == 0:
            x.balance_factor = 0
            z.balance_factor = 0
        else:
            x.balance_factor = 0
            z.balance_factor = -1
        y.balance_factor = 0
        return y

a = AVLTree()
a.insert(6)
a.insert(5)
a.insert(10)
a.insert(13)
a.insert(12)
