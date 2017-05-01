# task: given a list of integers, find the maximum number of integers you can
#       pick such that the absolute difference between any two integers is no larger than 1

def pick_number(l):
    d = dict()
    for i in l:
        d[i] = d.get(i, 0) + 1
    keys = []
    single_max = 0
    for k, v in d.items():
        if v > single_max:
            single_max = v
        keys.append(k)
    keys = merge_sort(keys)
    max_ints = 0
    for i in range(len(keys) - 1):
        if keys[i] + 1 == keys[i + 1]:
            a = d[keys[i]]
            b = d[keys[i + 1]]
            if a + b > max_ints:
                max_ints = a + b
    return max_ints if max_ints > single_max else single_max

def merge_sort(l):
    if not l or len(l) == 1:
        return l
    if len(l) == 2:
        if l[1] < l[0]:
            l[0], l[1] = l[1], l[0]
        return l
    else:
        mid = len(l) // 2
        left = merge_sort(l[:mid])
        right = merge_sort(l[mid:])
        return merge(left, right)

def merge(l, r):
    out = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            out.append(l[i])
            i += 1
        else:
            out.append(r[j])
            r += 1
    while i < len(l):
        out.append(l[i])
        i += 1
    while j < len(l):
        out.append(r[j])
        j += 1
    return out
