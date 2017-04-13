# basic node definition
class Node:
    def __init__(self, v=None, n=None):
        self.key = v
        self.next = n

# problem from stanford cs course
# count iteratively
def count(head):
    n = 0
    while head:
        n += 1
        head = head.next
    return n

# count recursively
def count_rec(n, c=0):
    if not n:
        return c
    else:
        return 1 + count_rec(n.next)

a = Node("c", Node("s", Node("i", Node("s", Node("c", Node("o", Node("o", Node("l"))))))))
print(count(a))
print(count_rec(a))
        
