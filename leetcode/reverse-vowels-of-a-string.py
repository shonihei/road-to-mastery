"""
Write a function that takes a string as input and reverse only the vowels of a string.
"""

def reverseVowels(s):
    s = list(s)
    vowels = "aeiouAEIOU"
    i = 0
    j = len(s) - 1
    while i < len(s) and j >= 0 and i < j:
        while i < len(s) and s[i] not in vowels:
            i += 1
        if i >= len(s) or i >= j:
            return ''.join(s)
        while j >= 0 and s[j] not in vowels:
            j -= 1
        if j < 0 or i >= j:
            return ''.join(s)
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return ''.join(s)


