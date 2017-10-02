"""
For a web developer, it is very important to know how to design a web page's size.
So, given a specific rectangular web page’s area, your job by now is to design a
rectangular web page, whose length L and width W satisfy the following requirements:

1. The area of the rectangular web page you designed must equal to the given target area.

2. The width W should not be larger than the length L, which means L >= W.

3. The difference between length L and width W should be as small as possible.
You need to output the length L and the width W of the web page you designed in sequence.
"""

import unittest

def constructRectangle(area):
    square_rooted = int(area ** 0.5)
    LW = [square_rooted, square_rooted]
    if LW[0] * LW[1] == area:
        return LW
    else:
        while True:
            LW[0] += 1
            if area % LW[0] == 0:
                LW[1] = area / LW[0]
                return LW

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual([2, 2], constructRectangle(4))
    
    def test2(self):
        self.assertEqual([300, 255], constructRectangle(76500))

if __name__ == "__main__":
    unittest.main()
