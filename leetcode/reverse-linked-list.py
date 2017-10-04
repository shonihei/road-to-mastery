"""
Reverse a singly linked list
"""

import unittest

class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

def create_LL(lst):
    if not lst:
        return None
    root = ListNode(lst[0])
    cur = root
    for i in range(1, len(lst)):
        cur.next = ListNode(lst[i])
        cur = cur.next
    return root

def collapse_LL(root, lst=None):
    if lst is None:
        lst = []
    if root:
        lst.append(root.val)
        collapse_LL(root.next, lst)
    return lst

def reverseList(head):
    if not head:
        return None
    prev = None
    _next = head.next
    while _next:
        head.next = prev
        prev = head
        head = _next
        _next = head.next
    head.next = prev
    return head

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            root = create_LL([4, 3, 6])
            root = reverseList(root)
            self.assertEqual(collapse_LL(root), [6, 3, 4])

        def test2(self):
            root = create_LL([])
            root = reverseList(root)
            self.assertEqual(collapse_LL(root), [])

        def test3(self):
            root = create_LL([1, 0, 23, 11, 53, 10, 4, 7, 9])
            root = reverseList(root)
            self.assertEqual(collapse_LL(root), [9, 7, 4, 10, 53, 11, 23, 0, 1])

    unittest.main()