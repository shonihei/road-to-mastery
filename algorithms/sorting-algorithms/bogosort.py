# just for the lols
# bogosort is the worst sorting algorithm but its simple.
# step 1: check whether list is sorted
# step 2: if it's not sorted, shuffle the list
# step 3: repeat

import sys, random

m = 0
def is_sorted(lst):
    global m
    for i in range(0, len(lst) - 1):
        m += 1
        if lst[i] > lst[i+1]:
            return False
    return True

def bogo_sort(lst):
    while not is_sorted(lst):
        random.shuffle(lst)
    return lst
    
lo, hi, n = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
l = random.sample(range(lo, hi), n)
print(l)
l = bogo_sort(l)
print("random list of {} elements sorted with {} comparisons".format(n, m))
print(l)
