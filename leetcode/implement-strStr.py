"""
Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""

def strStr(haystack, needle):
    if haystack == needle:
        return 0
    if len(needle) == 0:
        return 0
    if len(needle) > len(haystack):
        return -1
    for i in range(len(haystack)):
        if haystack[i] == needle[0]:
            j = i + 1
            for k in range(1, len(needle)):
                if j >= len(haystack):
                    break
                if needle[k] != haystack[j]:
                    break
                j += 1
            else:
                return i
    return -1

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            self.assertEqual(strStr("hello world baby!", "rld"), 8)
        
        def test2(self):
            self.assertEqual(strStr("hello world baby!", "rxld"), -1)

    unittest.main()