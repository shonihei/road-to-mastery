"""
Given an array of integers that is already sorted in ascending order, find
two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they
add up to the target, where index1 must be less than index2. Please note that your
returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may
not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""

import unittest

def twoSum(numbers, target):
    left = 0
    right = len(numbers) - 1
    while left < right:
        _sum = numbers[left] + numbers[right]
        if _sum == target:
            return [left + 1, right + 1]
        elif _sum < target:
            left += 1
        else:
            right -= 1

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(twoSum([2, 7, 11, 15], 9), [1, 2])

if __name__ == "__main__":
    unittest.main()