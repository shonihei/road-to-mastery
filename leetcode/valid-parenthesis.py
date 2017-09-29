"""
Given a string containing just the characters 
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" 
and "()[]{}" are all valid but "(]" and "([)]" are not.
"""

import unittest

def isValid(s):
    stack = []
    for c in s:
        if c == ")":
            if not stack or stack[-1] != "(":
                return False
            else:
                stack.pop()
        elif c == "}":
            if not stack or stack[-1] != "{":
                return False
            else:
                stack.pop()
        elif c == "]":
            if not stack or stack[-1] != "[":
                return False
            else:
                stack.pop()
        else:
            stack.append(c)
    if not stack:
        return True
    return False

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(isValid("({}){}((){})"), True)
    
    def test2(self):
        self.assertEqual(isValid("({}){}}((){})"), False)
    
    def test3(self):
        self.assertTrue(isValid("()[]{}"))

if __name__ == "__main__":
    unittest.main()