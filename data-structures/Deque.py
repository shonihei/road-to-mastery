# Deque implementation based on Java collection API

class Deque:
    class _Node:
        def __init__(self, v=None, n=None, p=None):
            self.key = v
            self.next_node = n
            self.prev_node = p

    def __init__(self):
        self.head = None
        self.tail = None
        self._count = 0

    def __len__(self):
        return self._count
        
    def append_right(self, item):
        if not self.tail:
            self.append_left(item)
            return
        self.tail.next_node = self._Node(item, None, self.tail)
        self.tail = self.tail.next_node
        self._count += 1
        
    def append_left(self, item):
        self.head = self._Node(item, self.head)
        if not self.tail:
            self.tail = self.head
        self._count += 1

    def contains(self, item):
        cur_node = self.head
        while cur_node:
            if cur_node.key == item:
                return True
            cur_node = cur_node.next_node
        return False

    def pop_left(self):
        if not len(self):
            raise IndexError("pop from empty deque")
        temp = self.head.key
        self.head = self.head.next_node
        self._count -= 1
        return temp

    def pop_right(self):
        if not len(self):
            raise IndexError("pop from empty deque")
        temp = self.tail.key
        self.tail = self.tail.prev_node
        self._count -= 1
        return temp
