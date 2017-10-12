"""
Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""

def prefix(s):
    p = [0 for i in range(len(s))]
    i = 0
    j = 1
    n = len(s)
    while j < n:
        if s[i] == s[j]:
            i += 1
            p[j] = i
            j += 1
        else:
            if i == 0:
                j += 1
            else:
                i = p[i - 1]
    return p

def strStr(haystack, needle):
    p = prefix(needle)
    j = 0
    for i in range(len(haystack)):
        while j > 0 and haystack[i] != needle[j]:
            j = p[j - 1]
        if haystack[i] == needle[j]:
            j += 1
        if j == len(needle):
            return i - (j - 1)
    return -1
            

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            self.assertEqual(strStr("hello world baby!", "rld"), 8)
        
        def test2(self):
            self.assertEqual(strStr("hello world baby!", "rxld"), -1)

    unittest.main()