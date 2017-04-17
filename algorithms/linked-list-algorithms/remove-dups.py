# task: given a linked unordered list, remove any duplicate values

# basic definition of a linked list node
class Node:
    def __init__(self, v=None, n=None):
        self.key = v
        self.next = n

# for debugging purposes
def print_ll(head):
    s = ""
    cur_node = head
    while cur_node:
        s += "{} -> ".format(cur_node.key)
        cur_node = cur_node.next
    s += "."
    print(s)
        
# O(n^2) soln with 3 pointers
# modified the original input
def remove_duplicate(head):
    i = head
    while i:
        j = i
        k = j.next
        while k:
            if k.key == i.key:
                k = k.next
                j.next = k
            else:
                j = k
                k = k.next
        i = i.next
    return head

A = Node(7, Node(7, Node(3, Node(7))))
print_ll(A)
remove_duplicate(A)
print_ll(A)
