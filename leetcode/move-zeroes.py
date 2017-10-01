"""
Given an array nums, write a function to move all 0's to the end
of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function,
nums should be [1, 3, 12, 0, 0].
"""

import unittest

def moveZeroes(nums):
    i = 0
    while i < len(nums):
        if nums[i] == 0:
            j = i + 1
            while j < len(nums):
                if nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
                j += 1
        i += 1

class Test(unittest.TestCase):
    def test1(self):
        nums = [0, 1, 0, 3, 12]
        out = [1, 3, 12, 0, 0]
        moveZeroes(nums)
        self.assertEqual(nums, out)

    def test2(self):
        nums = [0, 0, 0, 0, 12, 0]
        out = [12, 0, 0, 0, 0, 0]
        moveZeroes(nums)
        self.assertEqual(nums, out)

if __name__ == "__main__":
    unittest.main()