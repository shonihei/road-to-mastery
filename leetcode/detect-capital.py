"""
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

1. All letters in this word are capitals, like "USA".
2. All letters in this word are not capitals, like "leetcode".
3. Only the first letter in this word is capital if it has more than one letter, like "Google".
"""

import unittest

def detectCapitalUse(word):
    first = None
    all_upper = None
    for c in word:
        if first is None:
            first = True if c.isupper() else False
        else:
            if all_upper is None:
                all_upper = True if c.isupper() else False
                if not first and all_upper:
                    return False
            else:
                if not all_upper and c.isupper():
                    return False
                elif all_upper and c.islower():
                    return False
    return True
                


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(detectCapitalUse("USA"), True)
    
    def test2(self):
        self.assertEqual(detectCapitalUse("FlaG"), False)
    
    def test3(self):
        self.assertEqual(detectCapitalUse("helloworld"), True)

    def test4(self):
        self.assertEqual(detectCapitalUse("Hello"), True)

if __name__ == "__main__":
    unittest.main()
