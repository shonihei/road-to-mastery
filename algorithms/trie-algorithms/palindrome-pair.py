# task: given a list of words, find whether any two words can be concatenated together to form a palindrome

def is_palindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

def naive_palindrome_pair(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j and is_palindrome(lst[i] + lst[j]):
                return True
    return False
