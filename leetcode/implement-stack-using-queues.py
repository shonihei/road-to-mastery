"""
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Notes:
You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue),
as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
"""


class MyStack(object):
    def __init__(self):
        self.queue = []
        self.size = 0
    
    def push(self, x):
        self.queue.append(x)
        for i in range(self.size):
            self.queue.append(self.queue.pop(0))
        self.size += 1
    
    def pop(self):
        if self.empty():
            raise IndexError("pop from empty queue")
        self.size -= 1
        return self.queue.pop(0)

    def top(self):
        if self.empty():
            raise IndexError("queue empty!")
        return self.queue[0]

    def empty(self):
        return self.size == 0

