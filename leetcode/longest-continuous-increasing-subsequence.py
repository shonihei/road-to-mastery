"""
Given an unsorted array of integers, find the length of longest continuous increasing subsequence.
"""

def findLengthOfLCIS(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 1

    _max = 0

    i = 1
    count = 1
    while i < len(nums):
        if nums[i] > nums[i - 1]:
            count += 1
        else:
            if count > _max:
                _max = count
            count = 1
        i += 1
    if count > _max:
        _max = count
    return _max

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            self.assertEqual(findLengthOfLCIS([]), 0)

        def test2(self):
            self.assertEqual(findLengthOfLCIS([1]), 1)

        def test3(self):
            self.assertEqual(findLengthOfLCIS([1, 3, 5, 4, 7]), 3)

        def test4(self):
            self.assertEqual(findLengthOfLCIS([1,3,5,7]), 4)

    unittest.main()
