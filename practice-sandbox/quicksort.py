def quick_sort(lst):
    stack = [(0, len(lst) - 1)]
    while stack:
        begin, end = stack.pop()
        if end < 0 or begin > len(lst) - 1 or abs(end  - begin) <= 1:
            continue
        print(begin, end)
        lo = begin
        hi = end - 1
        pivot_index = end
        pivot_value = lst[pivot_index]
        while (lo < hi):
            while(lst[lo] < pivot_value):
                lo += 1
            while(lst[hi] > pivot_value):
                hi -= 1
            if lo <= hi:
                lst[lo], lst[hi] = lst[hi], lst[lo]
                lo += 1
                hi -= 1
        lst[lo], lst[pivot_index] = lst[pivot_index], lst[lo]
        stack.append((begin, hi))
        stack.append((hi+1, end))

import random
a = random.sample(range(0, 10), 10)
quick_sort(a)
