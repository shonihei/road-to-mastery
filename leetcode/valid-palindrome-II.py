"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
"""

def validPalindrome(s):
    return _validPalindrome(s)

def _validPalindrome(s, diff=False):
    if not s:
        return True
    if len(s) == 1:
        return True
    else:
        if s[0] == s[-1]:
            return _validPalindrome(s[1:-1], diff)
        else:
            if diff:
                return False
            else:
                return _validPalindrome(s[1:], True) or _validPalindrome(s[:-1], True)


if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            self.assertEqual(validPalindrome("abca"), True)
        
        def test2(self):
            self.assertEqual(validPalindrome("aba"), True)
        
        def test3(self):
            self.assertEqual(validPalindrome("hellloehh"), False)

        def test4(self):
            self.assertEqual(validPalindrome("abc"), False)
        
        def test5(self):
            self.assertEqual(validPalindrome("deeee"), True)

    unittest.main()