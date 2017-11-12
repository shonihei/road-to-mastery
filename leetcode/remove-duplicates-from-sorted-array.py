"""
Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
"""

def removeDuplicates(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	if not nums:
		return nums
	N = len(nums)
	cur_el = nums[0]
	start = 0
	count = 1
	i = 1
	while i < N:
		if nums[i] != cur_el:
			if count > 1:
				shiftLeft(nums, count - 1)
			cur_el = nums[i]
			count = 1
		else:
			count += 1
		i += 1

