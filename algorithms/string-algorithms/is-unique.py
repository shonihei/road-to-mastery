# task: write an algorithm to determine if a string contains
#       all unique characters

# O(n) time complexity with O(n) memory
def is_unique(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = True
        else:
            return False
    return True

# in-place O(n^2) soln with O(1) memory
def is_unique_2(s):
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True

A = "abcdefghijka"
print(is_unique(A))
print(is_unique_2(A))
B = "abcdefghijk"
print(is_unique(B))
print(is_unique_2(B))
