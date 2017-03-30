class MinHeap:
    def __init__(self):
        self.heap = []

    def get_left_child(index):
        return (2 * index) + 1

    def get_right_child(index):
        return (2 * index) + 2

    def get_parent(index):
        return (index - 1) // 2

    def insert(self, item):
        self.heap.append(item)
