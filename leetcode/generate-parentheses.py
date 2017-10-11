"""
[UNFINISHED]
Given n pairs of parentheses, write a function to generate
all combinations of well-formed parentheses.
"""

def generateParentheses(n):
    lst = []
    addParenthesis(lst, "", 0, n)
    return lst

def addParenthesis(lst, s, _open, close):
    if close:
        addParenthesis(lst, s + "(", _open + 1, close - 1)
    if _open:
        addParenthesis(lst, s + ")", _open - 1, close)
    if _open == 0 and close == 0:
        lst.append(s)