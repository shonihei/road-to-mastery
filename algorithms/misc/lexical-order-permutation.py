# task: given an iterable object (list and string), re-order the original list and return the next lexicographically largest permutation

def next_lexcal_order(l):
    x = -1
    for i in range(len(l) - 1):
        if l[i] < l[i + 1]:
            x = i
    if x == -1:
        return None
    y = x + 1
    for j in range(x + 1, len(l)):
        if l[x] < l[j]:
            y = j
    l[x], l[y] = l[y], l[x]
    l[x+1:] = l[-1:x:-1]
    return l

# generator function that yields a permutation until there are no more
def permute(l):
    if isinstance(l, str):
        l = list(l)
    x = -1
    for i in range(len(l) - 1):
        if l[i] < l[i + 1]:
            x = i
    yield l
    
    while x != -1:
        y = x + 1
        for j in range(x + 1, len(l)):
            if l[x] < l[j]:
                y = j
        l[x], l[y] = l[y], l[x]
        i, j = x + 1, len(l) - 1
        while i < j:
            l[i], l[j] = l[j], l[i]
            i += 1
            j -= 1
        yield l
        x = -1
        for i in range(len(l) - 1):
            if l[i] < l[i + 1]:
                x = i
