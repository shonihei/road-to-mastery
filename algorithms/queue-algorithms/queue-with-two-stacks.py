# task: implement a queue class using two stacks.

class Queue:
    def __init__(self):
        self.temp_buffer = []
        self.out_buffer = []

    def enqueue(self, v):
        self.temp_buffer.append(v)

    def dequeue(self):
        while self.temp_buffer:
            self.out_buffer.append(self.temp_buffer.pop())
        return self.out_buffer.pop()

    def peak(self):
        while self.temp_buffer:
            self.out_buffer.append(self.temp_buffer.pop())
        return self.out_buffer[-1]

    def __repr__(self):
        while self.temp_buffer:
            self.out_buffer.append(self.temp_buffer.pop())
        return str(self.out_buffer)
    
q = Queue()
