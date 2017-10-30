"""
Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""

def removeElement(nums, val):
    max_val = 0
    for num in nums:
        if num > max_val:
            max_val = num
    
    dum = max_val + 1
    for i in range(len(nums)):
        if nums[i] == val:
            nums[i] = dum
    
    nums.sort()
    length = 0
    for num in nums:
        if num == dum:
            return length
        length += 1
    return length