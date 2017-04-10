import sys, random

counter = 0
def selection_sort(lst):
    global counter
    for i in range(len(lst)):
        m = i
        for j in range(i, len(lst)):
            counter += 1
            if lst[j] < lst[m]:
                m = j
        lst[i], lst[m] = lst[m], lst[i]
    return lst

lo, hi, n = list(map(int, sys.argv[1:4]))
l = random.sample(range(lo, hi), n)
l = selection_sort(l)
print("random list of {} elements sorted with {} comparisons".format(n, counter))
print(l)
