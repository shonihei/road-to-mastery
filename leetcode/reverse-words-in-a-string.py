"""
Given a string, you need to reverse the order of characters
in each word within a sentence while still preserving whitespace
and initial word order.
"""

def reverseWords(s):
    lst = s.split(' ')
    out = ""
    for word in lst:
        for char in reversed(word):
            out += char
        out += " "
    return out[:-1]

print(reverseWords("Let's take LeetCode contest"))
