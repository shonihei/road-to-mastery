# task: given an array, reverse the order

def reverse(l):
    i = 0
    j = len(l) - 1
    while i < j:
        l[i], l[j] = l[j], l[i]
        i += 1
        j -= 1
    return l

A = ["E", "X", "A", "M", "P", "L", "E"]
print(''.join(A))
print(''.join(reverse(A)))
