# Stack implementation based on Java util interface

class Stack:
    class _Node:
        def __init__(self, val=None, n=None):
            self.key = val
            self.next_node = n

    def __init__(self):
        self.head = None
        self.count = 0

    def __repr__(self):
        if not self.count:
            return "[]"
        output = "["
        cur_node = self.head
        while cur_node.next_node:
            output += str(cur_node.key) + ", "
            cur_node = cur_node.next_node
        return output + str(cur_node.key) + "]"

    def empty(self):
        return self.count == 0

    def peek(self):
        if not self.count:
            raise IndexError("empty stack")
        return self.head.key

    def pop(self):
        if not self.count:
            raise IndexError("pop from empty list")
        temp = self.head.key
        self.head = self.head.next_node
        self.count -= 1
        return temp

    def push(self, item):
        self.head = self._Node(item, self.head)
        self.count += 1

    def search(self, item):
        counter = 0
        cur_node = self.head
        while cur_node:
            if cur_node.key == item:
                return counter
            counter += 1
            cur_node = cur_node.next_node
        return -1
        
def main():
    s = Stack()
    s.push(10)
    s.push(9)
    s.push(8)
    
if __name__ == "__main__":
    main()
