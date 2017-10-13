"""
Given a string, sort it in decreasing order based on the frequency of characters.
"""

from collections import Counter
def frequencySort(s):
    counter = Counter(s)
    out = ""
    for c, count in counter.most_common(len(counter)):
        out += (c * count)
    return out

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            self.assertEqual(frequencySort("tree"), "eetr")
    
    unittest.main()
