"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
"""

def merge(nums1, m, nums2, n):
	i = j = 0
	while i < m and j < n:
		if nums1[i] < num2[j]:
			i += 1
		else:
			shift(nums1, m, i)
			nums1[i] = nums2[j]
			m += 1
			i += 1
			j += 1
	while j < n:
		nums1[i] = nums2[j]
		i += 1
		j += 1

def shift(nums1, m, i):
	for j in range(m - 1, i - 1, -1):
		nums1[j+1] = nums1[j]
