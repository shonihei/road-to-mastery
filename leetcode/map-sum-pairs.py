"""
Implement a MapSum class with insert, and sum methods.

For the method insert, you'll be given a pair of (string, integer). The string represents
the key and the integer represents the value. If the key already existed, then the original key-value
pair will be overridden to the new one.

For the method sum, you'll be given a string representing the prefix, and you need to return the sum
of all the pairs' value whose key starts with the prefix.
"""

class Node(object):
    def __init__(self, val):
        self.val = val
        self.children = {}

class MapSum(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(0)
        # global dictionary to keep track of inserted keys
        self.dict = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        if key in self.dict:
            self._insert(self.root, key, val, 0, False)
        else:
            self._insert(self.root, key, val, 0, True)
        self.dict[key] = True

    def _insert(self, node, key, val, i, add):
        if i >= len(key):
            return
        else:
            if key[i] not in node.children:
                node.children[key[i]] = Node(val)
            else:
                if add:
                    node.children[key[i]].val += val
                else:
                    node.children[key[i]].val = val
            self._insert(node.children[key[i]], key, val, i+1, add)

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        return self._sum(self.root, prefix, 0)

    def _sum(self, cur_node, prefix, i):
        if not prefix:
            return 0
        if prefix[i] not in cur_node.children:
            return 0
        if i == len(prefix) - 1:
            return cur_node.children[prefix[i]].val
        else:
            return self._sum(cur_node.children[prefix[i]], prefix, i + 1)
