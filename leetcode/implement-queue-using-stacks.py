"""
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
"""

class MyQueue(object):
    def __init__(self):
        self.temp = []
        self.actual = []
        self.size = 0
    
    def push(self, x):
        self.temp.append(x)
        self.size += 1
    
    def pop(self):
        if self.size == 0:
            raise IndexError("Can't pop from empty queue")
        if not self.actual:
            self.flush_temp()
        self.size -= 1
        return self.actual.pop()
        
    def flush_temp(self):
        while self.temp:
            self.actual.append(self.temp.pop())
        
    def peek(self):
        if self.size == 0:
            raise IndexError("Can't peek into an empty Queue")
        if not self.actual:
            self.flush_temp()
        return self.actual[-1]

    def empty(self):
        return self.size == 0
