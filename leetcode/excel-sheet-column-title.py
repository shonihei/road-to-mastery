"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.
"""

def convertToTitle(n):
    return "" if n == 0 else convertToTitle((n - 1) // 26) + chr((n - 1) % 26 + ord('A'))
