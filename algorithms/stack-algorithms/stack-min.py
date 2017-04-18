# task: implement a stack which has a function to return the minimum element

class Node:
    def __init__(self, v=None, minimum=None):
        self.v = v
        self.min = minimum

class StackMin:
    def __init__(self):
        self.stack = []

    def push(self, v):
        if not self.stack:
            self.stack.append(Node(v, v))
        else:
            m = self.stack[-1].min
            if m < v:
                self.stack.append(Node(v, m))
            else:
                self.stack.append(Node(v, v))

    def get_min(self):
        return self.stack[-1].min

    def pop(self):
        if not self.stack:
            raise IndexError("popping from empty stack")
        return self.stack.pop().v

    def __repr__(self):
        s = "["
        for i in self.stack[:-1]:
            s += str(i.v) + ", "
        s += str(self.stack[-1].v) + "]"
        return s

A = StackMin()
A.push(4)
A.push(7)
A.push(5)
A.push(6)
A.push(3)
A.push(1)
