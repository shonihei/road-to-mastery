"""
Given two sequences, find the length of longest subsequence present in both of them.
A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.
For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”. So a string of
length n has 2^n different possible subsequences.
"""

memo = {}
def LCS(A, B):
    if (A, B) in memo:
        return memo[(A, B)]
    else:
        if len(A) == 0 or len(B) == 0:
            return 0
        if A[-1] == B[-1]:
            memo[(A, B)] = LCS(A[:-1], B[:-1]) + 1
        else:
            memo[(A, B)] = max(LCS(A, B[:-1]), LCS(A[:-1], B))
        return memo[(A, B)]

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            self.assertEqual(LCS("", ""), 0)
        
        def test2(self):
            self.assertEqual(LCS("ABCDEFG", "ACTEFSG"), 5)

    unittest.main()

