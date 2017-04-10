# completed
# Problem : https://www.hackerrank.com/challenges/fibonacci-modified
#
# The key to solving this problem was to use memoization technique to make sure that
# no input was being calculated more than once. Although this problem can easily be
# solved without memoization using very naive recursive function, with large n, it
# would be impractical

t0, t1, n = list(map(int, input().strip().split(' ')))

d = {}
def fibonacci_modified(t0, t1, n):
    d[0] = t0
    d[1] = t1
    return fibonacci_modified_aux(n-1)
    
def fibonacci_modified_aux(n):
    if n in d:
        return d[n]
    else:
        d[n] = fibonacci_modified_aux(n-2) + (fibonacci_modified_aux(n-1) ** 2)
        return d[n]
    
print(fibonacci_modified(t0, t1, n))
