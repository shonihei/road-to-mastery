"""
[UNFINISHED]
Given n pairs of parentheses, write a function to generate
all combinations of well-formed parentheses.
"""

def generateParentheses(n):
    if n == 0:
        return ""
    elif n == 1:
        return "()"
    else:
        left = generateParentheses(n - 1) + "()"
        middle = "(" + generateParentheses(n - 1) + ")"
        print(left)
        print(middle)
        return left
