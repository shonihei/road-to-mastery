#task: given two linked lists each of which represents a string. Return 0 if they are the same,
#      1 if the first string is lexicographically greater than the second, -1 if the second is
#      lexicographically less than the second.

class Node:
    def __init__(self, v=None, n=None):
        self.key = v
        self.next = n

def compr(h1, h2):
    while h1 and h2:
        if h1.key != h2.key:
            return -1 if h1.key < h2.key else 1
        h1 = h1.next
        h2 = h2.next
    if not h1 and not h2:
        return 0
    return -1 if not h1 and h2 else 1

A = Node("h", Node("e", Node("l", Node("l", Node("o")))))
B = Node("h", Node("e", Node("l", Node("l", Node("j")))))
print(compr(A, B))
print(compr(A, A))
