# Problem : https://www.hackerrank.com/challenges/fibonacci-modified

t0, t1, n = list(map(int, input().strip().split(' ')))

def fibonacci_modified(t0, t1, n):
    if n == 1:
        return t0
    elif n == 2:
        return t1
    else:
        return fibonacci_modified(t0, t1, n - 2) + (fibonacci_modified(t0, t1, n - 1) ** 2)

print(fibonacci_modified(t0, t1, n))
