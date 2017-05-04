import sys, random

counter = 0

def wrapper(l):
    lst = quick_sort(l[:])
    return lst

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

def percent_sorted(u, s):
    c = 0
    for i in range(len(u)):
        j = s.index(u[i])
        if i <= j:
            c += 1
    return c / len(u)

def test(lo, hi, n, test_size):
    global buckets
    global counter
    buckets = dict()
    for test in range(test_size):
        l = random.sample(range(lo, hi), n)
        sorted_lst = wrapper(l)
        percent_same = percent_sorted(l, sorted_lst)
        buckets[percent_same] = buckets.get(percent_same, []) + [counter]
        counter = 0
    for k, v in sorted(buckets.items()):
        avg = sum(v) / len(v)
        print("{:.2f}% sorted: {:.2f} comparisons".format(k * 100, avg))
        
#print("original list is {}% sorted".format(percent_same * 100))
#print("original: {}".format(str(l)))
#print("sorted  : {}".format(str(sorted_lst)))
#print("random list of {} elements sorted with {} comparisons".format(n, counter))
