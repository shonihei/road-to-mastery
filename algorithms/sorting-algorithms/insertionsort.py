import random, sys

m = 0 # keeps track of number of comparisons

def wrapper(l):
    lst = l[:]
    insertion_sort(lst)
    return lst

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

def percent_sorted(u, s):
    c = 0
    for i in range(len(u)):
        j = s.index(u[i])
        if i <= j:
            c += 1
    return c / len(u)

def test(lo, hi, n, test_size):
    global buckets
    global m
    buckets = dict()
    worst_case = n**2
    for test in range(test_size):
        l = random.sample(range(lo, hi), n)
        sorted_lst = wrapper(l)
        percent_same = m / worst_case
        buckets[percent_same] = buckets.get(percent_same, []) + [m]
        m = 0
    for k, v in sorted(buckets.items()):
        avg = sum(v) / len(v)
        print("{:.2f}% sorted: {:.2f} comparisons".format(k * 100, avg))
            
#lo, hi, n = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
#l = random.sample(range(lo, hi), n)
#insertion_sort(l)
#print("random list of {} elements sorted with {} comparisons".format(n, m))
#print(l)
