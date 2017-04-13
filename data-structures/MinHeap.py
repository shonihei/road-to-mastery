class MinHeap:
    def __init__(self):
        # this heap is implemented using one-indexing
        # for faster child and parent index calculation
        self.heap = [0]
        self.count = 0

    def __repr__(self):
        return str(a.heap[1:])
    
    def insert(self, v):
        self.heap.append(v)
        self.count += 1
        self.heapify_up(self.count)

    def heapify_up(self, i):
        while i // 2 > 0:
            if self.heap[i] < self.heap[i // 2]:
                self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i //= 2

    def heapify_down(self, i):
        while i * 2 <= self.count:
            m = i * 2 # default min child to left child
            if m + 1 < self.count and self.heap[m+1] < self.heap[m]:
                m += 1
            if self.heap[i] < self.heap[m]:
                break
            self.heap[i], self.heap[m] = self.heap[m], self.heap[i]
            i = m
            
    def del_min(self):
        if self.count == 0:
            raise IndexError("cannot delete from empty heap")
        self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]
        del self.heap[-1]
        self.count -= 1
        self.heapify_down(1)

    def get_min(self):
        r = self.heap[1]
        self.del_min()
        return r
