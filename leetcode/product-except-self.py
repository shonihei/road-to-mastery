"""
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to
the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].
"""

def productExceptSelf(nums):
    out = [1 for i in range(len(nums))]
    m = 1
    for i in range(len(out)):
        out[i] = m
        m *= nums[i]
    m = 1
    for i in range(len(out) - 1, -1, -1):
        out[i] *= m
        m *= nums[i]
    return out