"""
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5

"""

class ListNode(object):
	def __init__(self, x, _next=None):
		self.val = x
		self.next = _next

def removeElements(head, val):
	"""
	:type head: ListNode
	:type val: int
	:rtype: ListNode
	"""
	while head is not None and head.val == val:
		head = head.next
	if head is None:
		return head
	i = head
	while i is not None and i.next is not None:
		if i.next.val == val:
			j = i.next
			while j is not None and j.val == val:
				j = j.next
			i.next = j
		i = i.next
	return head

l = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))

def print_ll(head):
	cur = head
	s = ""
	while cur:
		s += str(cur.val) + "->"
		cur = cur.next
	print(s + ".")