# task: given a string, check if it a permutation of a palindrome

# O(n) soln with O(n) spatial complexity
def palindrome_permutation(s):
    # build dictionary with counter as a value
    d = dict()
    for c in s:
        if c == " ":
            continue
        d[c] = d.get(c, 0) + 1

    # flag variable
    odd_ball_found = False
    for k, v in d.items():
        if v % 2 != 0:
            if not odd_ball_found:
                odd_ball_found = True
            else:
                return False
    return True 

A = "taco cat"
B = "hello!"
C = "helloheo!!"
print(palindrome_permutation(A))
print(palindrome_permutation(B))
print(palindrome_permutation(C))
