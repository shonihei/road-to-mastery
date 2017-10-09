"""
Given an integer array, you need to find one continuous subarray that if you only sort this subarray
in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.
"""

def findUnsortedSubarray(nums):
    if len(nums) <= 1:
        return 0
    i = 0
    while i < len(nums) - 1:
        if nums[i] >= nums[i + 1]:
            break
        i += 1
    
    j = len(nums) - 1
    while j > 0:
        if nums[j] <= nums[j - 1]:
            break
        j -= 1
    l = j - i + 1
    if l < 0:
        return 0
    return l

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            self.assertEqual(findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]), 5)

        def test2(self):
            self.assertEqual(findUnsortedSubarray([2, 3, 4, 5, 6]), 0)

        def test3(self):
            self.assertEqual(findUnsortedSubarray([0]), 0)

        def test4(self):
            self.assertEqual(findUnsortedSubarray([]), 0)

        def test5(self):
            self.assertEqual(findUnsortedSubarray([2, 1]), 2)
        
        def test6(self):
            self.assertEqual(findUnsortedSubarray([1, 3, 2, 2, 2]), 4)
    
    unittest.main()