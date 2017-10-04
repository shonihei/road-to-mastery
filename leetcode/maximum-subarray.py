"""
Find the contiguous subarray within an array (containing at least one number)
which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""

def maxSubArray(nums):
    running_sum = _max = nums[0]
    for i in range(1, len(nums)):
        if running_sum + nums[i] > nums[i]:
            running_sum += nums[i]
        else:
            running_sum = nums[i]
        if running_sum > _max:
            _max = running_sum
    return _max

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            self.assertEqual(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]), 6)

    unittest.main()