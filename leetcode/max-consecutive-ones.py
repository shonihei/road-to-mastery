"""
Given a binary array, find the maximum number of consecutive 1s in this array.
"""

def findMaxConsecutiveOnes(nums):
    _max = 0
    cur_count = 0
    for num in nums:
        if num == 1:
            cur_count += 1
            _max = max(_max, cur_count)
        else:
            cur_count = 0
    return _max

print(findMaxConsecutiveOnes([1,1,0,1,1,1]))
