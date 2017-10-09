"""
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
"""

def checkPossibility(nums):
    diffs = [nums[i] - nums[i - 1] for i in range(1, len(nums)) if (nums[i] - nums[i - 1]) < 0]
    return True if len(diffs) <= 1 else False
    
