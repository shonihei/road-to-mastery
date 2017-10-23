"""
Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.
"""

def canPlaceFlowers(flowerbed, n):
    planted = 0
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0:
            left = True if i - 1 < 0 or flowerbed[i - 1] == 0 else False
            right = True if i + 1 >= len(flowerbed) or flowerbed[i + 1] == 0 else False
            if left and right:
                flowerbed[i] = 1
                planted += 1
    return n <= planted

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            self.assertTrue(canPlaceFlowers([1, 0, 0, 0, 1], 1))
        
        def test2(self):
            self.assertFalse(canPlaceFlowers([1, 0, 0, 0, 1], 2))
    
    unittest.main()