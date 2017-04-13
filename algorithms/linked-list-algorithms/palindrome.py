# task: give a linked list, figure out whether the
#       values stored in them would create a palindrome

class Node:
    # basic node definition
    def __init__(self, v=None, n=None):
        self.key = v
        self.next = n

# naive solution that takes O(n) time and O(n) space
# O(n) to create a list of nodes
# O(n) to reverse the list and compare with the original list
def check_palindrome(head):
    # if linked list is empty, it's palindrome
    if not head:
        return True
    else:
        l = []
        cur_node = head
        while cur_node:
            l.append(cur_node.key)
            cur_node = cur_node.next
        if list(reversed(l)) == l:
            return True
        return False

