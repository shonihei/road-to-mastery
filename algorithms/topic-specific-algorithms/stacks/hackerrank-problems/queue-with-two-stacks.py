# Problem: https://www.hackerrank.com/challenges/queue-using-two-stacks
# Not Complete

class Queue:
    def __init__(self):
        self.A = []
        self.B = []

    def enqueue(self, val):
        self.B.append(val)

    def flushB(self):
        while self.B:
            self.A.append(self.B.pop())

    def dequeue(self):
        if self.B:
            self.flushB()
        if not self.A:
            raise IndexError('dequeue from empty queue')
        return self.A.pop()
