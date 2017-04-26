# task: given a list of stacks, find the maximum height such that all the stacks are equal in height

def find_max_height(l):
    s = [sum(x) for x in l]
    while all(l):
        max_i = 0
        max_v = s[0]
        equal = True
        for i in range(1, len(s)):
            if max_v != s[i]:
                equal = False
            if s[i] > max_v:
                max_v = s[i]
                max_i = i
        if equal:
            return s[0]
        s[max_i] -= l[max_i].pop()
    return 0
    
A = [[1, 1, 1, 2, 3],
     [1, 3, 4],
     [1, 7, 1, 1]]
B = [[10, 1, 3, 1, 1],
     [4, 5, 1, 3, 2, 6],
     [1, 1, 1, 4, 3, 1]]
print(find_max_height(A))
print(find_max_height(B))
