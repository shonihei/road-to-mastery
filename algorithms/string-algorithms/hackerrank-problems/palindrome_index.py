# task: write a function that takes a string and returns what
#       index to delete in order to turn the string into a palindrome.
#       if the given string is already a palindrome, return -1
#       if there's no letter that you can delete to make a palindrom return -1
#       else return its index
# sample:
#       "abcba" -> -1      already a palindrome
#       "abcca" -> 1       deleting b would make it a palindrome
#       "abcde" -> -1      cannot make a palindrome

def is_pal(s):
    i = 0
    j = len(s) - 1
    for n in range(len(s) // 2):
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

# O(n^2) solution
def palindrome_index(s):
    if is_pal(s):
        return -1
    for i in range(len(s)):
        new_s = s[:i] + s[i+1:]
        if is_pal(new_s):
            return i
    return -1

# Another O(n^2) solution
def palindrome_index_2(s):
    if is_pal(s):
        return -1
    l = []
    for i in range(len(s)):
        l.append(s[:i]+s[i+1:])
    for i, s in enumerate(l):
        if is_pal(s):
            return i
    return -1

# Another O(n^2) solution
# performs better than previous two because
# we only check whether something is a palindrome when we spot mismatching characters
def palindrome_index_3(s):
    if len(s) == 0:
        return -1
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            if is_pal(s[:i] + s[i+1:]):
                return i
            elif is_pal(s[:j] + s[j+1:]):
                return j
            return -1
    return -1

import time
S = "abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbsa"
s = time.time()
r = palindrome_index(S)
e = time.time()
print("testing with string of length {}".format(len(S)))
print("1st soln took {}s and returned {}".format(e - s, r))
s = time.time()
r = palindrome_index_2(S)
e = time.time()
print("2nd soln took {}s and returned {}".format(e - s, r))
s = time.time()
r = palindrome_index_3(S)
e = time.time()
print("3rd soln took {}s and returned {}".format(e - s, r))
