"""
Given an array of integers, every element appears twice except for one. Find that single one.
"""

def singleNumber(nums):
    answer = 0
    for num in nums:
        answer ^= num
    return answer

l = [2, 3, 4, 4, 3, 6, 2]
print(singleNumber(l))

l = [1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]
print(singleNumber(l))