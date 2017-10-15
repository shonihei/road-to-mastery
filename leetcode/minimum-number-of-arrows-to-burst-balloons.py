"""
There are a number of spherical balloons spread in two-dimensional space. For each balloon,
provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal,
y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice.
Start is always smaller than end. There will be at most 104 balloons.

An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with
xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number
of arrows that can be shot. An arrow once shot keeps travelling up infinitely. The problem is to
find the minimum number of arrows that must be shot to burst all balloons.
"""

def findMinArrowShots(points):
    if not points:
        return 0
    points.sort(key=lambda x: x[0])
    count = 0
    arrow_range = points[0]
    for i in range(1, len(points)):
        start, end = points[i]
        if start <= arrow_range[1]:
            arrow_range[0] = start
            if end < arrow_range[1]:
                arrow_range[1] = end
        else:
            count += 1
            arrow_range = [start, end]
    return count + 1

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            a = [[10,16], [2,8], [1,6], [7,12]]
            self.assertEqual(findMinArrowShots(a), 2)
        
        def test2(self):
            a = [[1, 20], [2, 18], [3, 25]]
            self.assertEqual(findMinArrowShots(a), 1)
        
        def test3(self):
            a = [[1,2],[2,3],[3,4],[4,5]]
            self.assertEqual(findMinArrowShots(a), 2)

    unittest.main()
