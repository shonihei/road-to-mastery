import sys, random

counter = 0
def quick_sort(lst):
    global counter
    
    if len(lst) <= 1:
        return lst
    elif len(lst) == 2:
        if lst[1] < lst[0]:
            lst[0], lst[1] = lst[1], lst[0]
        return lst
    else:
        pivot = len(lst) - 1
        lo = 0
        hi = pivot - 1
        done = False
        while True:
            while lst[lo] < lst[pivot]:
                counter += 1
                lo += 1
                if lo > hi:
                    done = True
                    break
            if done:
                break
            while lst[hi] > lst[pivot]:
                counter += 1
                hi -= 1
                if hi < lo:
                    done = True
                    break
            if done:
                break
            lst[lo], lst[hi] = lst[hi], lst[lo]
        lst[lo], lst[pivot] = lst[pivot], lst[lo]
        pivot = lo
        counter += 2
        return quick_sort(lst[:pivot]) + [lst[pivot]] + quick_sort(lst[pivot + 1:])

lo, hi, n = list(map(int, sys.argv[1:4]))
l = random.sample(range(lo, hi), n)
l = quick_sort(l)
print("random list of {} elements sorted with {} comparisons".format(n, counter))
print(l)
