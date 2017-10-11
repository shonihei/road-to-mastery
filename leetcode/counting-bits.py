"""
Given a non negative integer number num. For every numbers i in
the range 0 ≤ i ≤ num calculate the number of 1's in their binary
representation and return them as an array.
"""

def countBits(num):
    out = [0 for i in range(num + 1)]
    recent_exponent = 2
    for i in range(1, num + 1):
        if i == 1 or i == 2:
            out[i] = 1 
        else:
            if i - recent_exponent == recent_exponent:
                recent_exponent = i
                out[i] = 1
            else:
                out[i] = out[recent_exponent] + out[i - recent_exponent]
    return out

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            self.assertEqual(countBits(5), [0, 1, 1, 2, 1, 2])
        
        def test2(self):
            self.assertEqual(countBits(11), [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3])
        
    unittest.main()