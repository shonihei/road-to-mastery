"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Now your job is to find the total Hamming distance between all pairs of the given numbers.
"""

def totalHammingDistance(nums):
    return sum(b.count('0') * b.count('1') for b in zip(*map('{:032b}'.format, nums)))

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            self.assertEqual(totalHammingDistance([4, 14, 2]), 6)
    
    unittest.main()
