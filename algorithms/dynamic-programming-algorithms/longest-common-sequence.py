# task: given two sequences, find the length of longest subsequence present in both of them

count = 0
def naive_LCS(s1, s2):
    global count
    count += 1
    if not s1 or not s2:
        return 0
    elif s1[-1] == s2[-1]:
        return 1 + naive_LCS(s1[:-1], s2[:-1])
    else:
        return max(naive_LCS(s1, s2[:-1]), naive_LCS(s1[:-1], s2))

def memoized_LCS(s1, s2):
    d = dict()
    c = 0
    def LCS(s1, s2):
        nonlocal c
        c += 1
        if not s1 or not s2:
            return 0
        if (s1, s2) in d:
            return d[(s1, s2)]
        elif s1[-1] == s2[-1]:
            i = (s1[:-1], s2[:-2])
            if i not in d:
                d[i] = 1 + LCS(i[0], i[1])
            return d[i]
        else:
            return max(LCS(s1, s2[:-1]), LCS(s1[:-1], s2))
    return LCS(s1, s2), c
