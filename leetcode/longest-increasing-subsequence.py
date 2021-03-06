"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note 
that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.
"""

def lengthOfLIS(nums):
    l = [1 for i in range(len(nums))]
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                l[i] = max(l[i], l[j] + 1)
    return max(l)
