# task: write an algorithm to check if two strings are permutation of each other

# O(n log n) soln
def is_permutation(s1, s2):
    if len(s1) != len(s2):
        return False
    s1 = sorted(s1)
    s2 = sorted(s2)
    for i, j in zip(s1, s2):
        if i != j:
            return False
    return True

A = "hello"
B = "elhlo"
C = "loloh"
print(is_permutation(A, B))
print(is_permutation(A, C))
