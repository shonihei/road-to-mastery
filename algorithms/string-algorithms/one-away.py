# task: given two string, determine if the strings are at most one edits from each other
#       'edit' refers to a deletion, insertion or replacement

def one_away(src, s):
    if abs(len(src) - len(s)) > 1:
        return False
    if len(src) == len(s):
        diff = False
        for i, j in zip(src, s):
            if i != j:
                if not diff:
                    diff = True
                else:
                    return False
        return True
    if len(src) < len(s):
        s, src = src, s
    j = 0
    diff = False
    for i in range(len(s)):
        if s[i] != src[j]:
            if not diff:
                diff = True
            else:
                return False
        else:
            j += 1
    return True

A = "helloworld"
B = "jelloworld"
C = "bellomold"
D = "jellowold"
print(one_away(A, B))
print(one_away(B, C))
print(one_away(B, D))
