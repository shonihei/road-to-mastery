"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array),
some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?
"""

import unittest

def findDuplicates(nums):
    out = []
    for n in nums:
        if nums[abs(n) - 1] < 0:
            out.append(abs(n))
        else:
            nums[abs(n) - 1] *= -1
    for n in nums:
        if nums[abs(n) - 1] < 0:
            nums[abs(n) - 1] *= -1
    return out

class Test(unittest.TestCase):
    def test1(self):
        a = [4, 3, 2, 7, 8, 2, 3, 1]
        self.assertEqual(findDuplicates(a), [2, 3])

if __name__ == "__main__":
    unittest.main()
