"""
Given an array consisting of n integers, find the contiguous subarray of given length k that has the
maximum average value. And you need to output the maximum average value.
"""

def findMaxAverage(nums, k):
    _sum = 0
    for i in range(k):
        _sum += nums[i]
    _max = _sum / (k + 0.0)
    i = 0
    j = i + k - 1
    while j < len(nums) - 1:
        j += 1
        _sum -= nums[i]
        _sum += nums[j]
        i += 1
        m = _sum / (k + 0.0)
        if m > _max:
            _max = m
    return _max

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            self.assertEqual(findMaxAverage([2, 4, -1, 10, 15], 1), 15)

    unittest.main()
