class Node:
    def __init__(self, v=None, n=None):
        self.key = v
        self.next = n

# iteratively get the nth element
def get_Nth(node, n):
    while n != 0:
        if not node.next:
            raise IndexError("n is larger than the length of the list")
        node = node.next
        n -= 1
    return node.key

def get_Nth_rec(node, n):
    if not node:
        raise IndexError("n is larger than the length of the list")
    if n == 0:
        return node.key
    else:
        return get_Nth_rec(node.next, n-1)

a = Node("a", Node("b", Node("c", Node("d"))))
print(get_Nth(a, 2))
print(get_Nth_rec(a, 2))
