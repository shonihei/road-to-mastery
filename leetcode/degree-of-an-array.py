"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
"""

def findShortestSubArray(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	d = {}
	for i in range(len(nums)):
		try:
			d[nums[i]][0] += 1
			d[nums[i]][2] = i
		except KeyError:
			d[nums[i]] = [1, i, i]
	min_len = float('inf')
	max_freq = 0
	for k, v in d.items():
		if v[0] > max_freq:
			min_len = v[2] - v[1] + 1
			max_freq = v[0]
		if v[0] == max_freq:	
			if v[2] - v[1] + 1 < min_len:
				min_len = v[2] - v[1] + 1
	return min_len