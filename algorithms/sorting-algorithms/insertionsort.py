import random, sys

m = 0 # keeps track of number of comparisons

def insertion_sort(lst):
    global m
    for i in range(1, len(lst)):
        cur = i
        for j in range(i - 1, -1, -1):
            m += 1
            if lst[cur] < lst[j]:
                lst[cur], lst[j] = lst[j], lst[cur]
                cur -= 1
            else:
                break
    return lst

lo, hi, n = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
l = random.sample(range(lo, hi), n)
l = insertion_sort(l)
print("random list of {} elements sorted with {} comparisons".format(n, m))
print(l)
