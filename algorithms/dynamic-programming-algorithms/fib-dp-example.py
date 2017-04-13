import sys
import time

memoized = 0
naive = 0
linear = 0

d = {
    1:1,
    2:1
}
# fibonacci sequence calculated using an iterative approach but
# previously calculated values are memoized
def fib_memoized(k):
    global memoized
    memoized += 1
    if k in d:
        return d[k]
    else:
        d[k] = k if k < 2 else fib_memoized(k - 2) + fib_memoized(k - 1)
        return d[k]

# naive recursive approach to solving the problem
def fib_naive(k):
    global naive
    naive += 1
    return k if k < 2 else fib_naive(k - 2) + fib_naive(k - 1)

# fibonacci sequence in linear time
# rather than using recursion, it uses iterative approach
def fib_linear(k):
    global linear
    a = 1
    b = 1
    if k < 0:
        raise("invalid k")
    elif k == 0:
        return a
    elif k == 1:
        return b
    else:
        for i in range(2, k):
            linear += 1
            c = a + b
            a = b
            b = c
        return b

k = int(sys.argv[1])
start = time.time()
fib_memoized(k)
end = time.time()
m = end - start
start = time.time()
fib_naive(k)
end = time.time()
n = end - start
start = time.time()
fib_linear(k)
end = time.time()
o = end - start
print("naive solution called {} times: {}s".format(naive, n))
print("memoized solution called {} times: {}s".format(memoized, m))
print("linear solution called {} times: {}s".format(linear, o))
