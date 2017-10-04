"""
[UNFINISHED]
Given n non-negative integers a1, a2, ..., an, where each represents a
point at coordinate (i, ai). n vertical lines are drawn such that the two
endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together
with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""

import unittest

def maxArea(height):
    max_height = height[0]
    max_area = local_area = 0
    for i in range(len(height) - 1):
        cur = height[i]
        _next = height[i + 1]
        local_area += max_height - _next
        if _next > cur:
            max_height = _next
            if max_area < local_area:
                max_area = local_area
    return max_area

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(maxArea([2, 0, 4, 6]), 4)

if __name__ == "__main__":
    unittest.main()

        
