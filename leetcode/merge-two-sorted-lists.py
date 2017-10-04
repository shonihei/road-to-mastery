"""
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes 
of the first two lists.
"""

class ListNode(object):
    def __init__(self, x, _next=None):
        self.val = x
        self.next = _next

def create_linked_list(lst):
    root = ListNode(lst[0])
    cur = root
    for i in range(1, len(lst)):
        cur.next = ListNode(lst[i])
        cur = cur.next
    return root

def convert_to_list(ll, lst=None):
    if lst is None:
        lst = []
    if ll:
        lst.append(ll.val)
        convert_to_list(ll.next, lst)
        return lst

def mergeTwoLists(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    if l1.val < l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            l1 = create_linked_list([2, 4, 6])
            l2 = create_linked_list([3, 10, 15, 20])
            merged = mergeTwoLists(l1, l2)
            soln = [2, 3, 4, 6, 10, 15, 20]
            self.assertEqual(convert_to_list(merged), soln)

        def test2(self):
            l1 = None
            l2 = create_linked_list([3, 10, 15, 20])
            merged = mergeTwoLists(l1, l2)
            soln = [3, 10, 15, 20]
            self.assertEqual(convert_to_list(merged), soln)
    
    unittest.main()