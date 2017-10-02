"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.
"""

import unittest

def intersection(nums1, nums2):
    d = dict()
    out = []
    for num in nums1:
        d[num] = True
    
    for num in nums2:
        if num in d and d[num] == True:
            out.append(num)
            d[num] = False
    return out

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(intersection([1, 2, 2, 1], [2, 2]), [2])
    
if __name__ == "__main__":
    unittest.main()
