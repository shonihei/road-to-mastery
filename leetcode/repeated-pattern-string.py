"""
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple
copies of the substring together. You may assume the given string consists of lowercase English letters only
and its length will not exceed 10000.
"""

def repeatedSubstringPattern(s):
    if not s:
        return True
    string = (s + s)[1:-1]
    return string.find(s) != -1

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            self.assertEqual(repeatedSubstringPattern("ababab"), True)
        
        def test2(self):
            self.assertEqual(repeatedSubstringPattern("abababa"), False)

    unittest.main()
