import sys
import time

memoized = 0
naive = 0

d = {
    1:1,
    2:1
}
def fib_memoized(k):
    global memoized
    memoized += 1
    if k in d:
        return d[k]
    else:
        d[k] = k if k < 2 else fib_memoized(k - 2) + fib_memoized(k - 1)
        return d[k]

def fib_naive(k):
    global naive
    naive += 1
    return k if k < 2 else fib_naive(k - 2) + fib_naive(k - 1)

k = int(sys.argv[1])
start = time.time()
fib_memoized(k)
end = time.time()
m = end - start
#start = time.time()
#fib_naive(k)
#end = time.time()
#n = end - start
#print("naive solution called {} times: {}s".format(naive, n))
print("memoized solution called {} times: {}s".format(memoized, m))
