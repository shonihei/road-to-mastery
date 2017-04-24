# task: given a string s and a substring p, find all valid shifts such that s[n...n+|p|] is equal to p

def naive_string_match(s, p):
    print("finding {} in {}".format(p, s))
    for i in range(len(s) - len(p) + 1):
        print("\tcomparing {} and {}...".format(s[i:len(p) + i], p))
        if s[i:len(p) + i] == p:
            return i
    return -1

def rabin_karp(s, p):
    print("finding {} in {}".format(p, s))
    h = hash(p)
    print("\t{}'s hash : {}".format(p, h))
    for i in range(len(s) - len(p) + 1):
        print("\tcomparing {} and {}...".format(hash(s[i:len(p) + i]), h))
        if hash(s[i:len(p) + i] == p):
            return i
    return -1

def knuth_morris_pratt(s, p):
    pi = prefix_function(p)
    out = []
    i = 0
    j = 0
    while i < len(s):
        if s[i] == p[j]:
            i += 1
            j += 1
        if j == len(p):
            out.append(i - j)
            j = pi[j - 1]
        elif i < len(s) and p[j] != s[i]:
            if j > 0:
                j = pi[j - 1]
            else:
                i += 1
    return out
    
def prefix_function(s):
    pi = [0 for i in range(len(s))]
    i = 0
    j = 1
    while j < len(s):
        if s[i] != s[j]:
            if i == 0:
                j += 1
                continue
            i = pi[i - 1]
        else:
            i += 1
            pi[j] = i
            j += 1
    return pi
    
a = "abcccbabcccaaabbcbcc"
print(naive_string_match(a, "cca"))
print("")
print(rabin_karp(a, "cca"))
print("")
print(knuth_morris_pratt(a, "ab"))
