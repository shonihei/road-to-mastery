"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""

class ListNode(object):
	def __init__(self, x, _next=None):
		self.val = x
		self.next = _next

def deleteDuplicates(head, prev=None):
	if head is None:
		return head
	else:
		if prev is None:
			head.next = deleteDuplicates(head.next, head.val)
		else:
			if head.val == prev:
				head = deleteDuplicates(head.next, prev)
			else:
				head.next = deleteDuplicates(head.next, head.val)
		return head

ll = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))

def print_ll(head):
	cur = head
	while cur:
		print(cur.val)
		cur = cur.next