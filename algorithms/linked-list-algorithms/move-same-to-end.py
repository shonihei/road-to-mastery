# task: given a linked list and a key k, move all occurrences of k to the end of the list

class Node:
    def __init__(self, v=None, n=None):
        self.key = v
        self.next = n

def move_to_end(node, k):
    
