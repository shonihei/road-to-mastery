"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""

def hasCycle(head):
    if not head:
        return False
    s = head
    f = head.next
    while f:
        if s == f:
            return True
        else:
            f = f.next
            if not f:
                return False
            f = f.next
            s = s.next
    return False
