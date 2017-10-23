"""
Count the number of prime numbers less than a non-negative number, n.
"""

def countPrimes(n):
    import math
    lst = [1 for i in range(2, n)]
    lst = [0, 0] + lst
    for i in range(2, int(math.sqrt(n))):
        if lst[i] == 1:
            j = i ** 2
            while j < n:
                lst[j] = 0
                j += i
    return lst

