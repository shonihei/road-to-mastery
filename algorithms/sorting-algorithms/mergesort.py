import sys, random

counter = 0
def merge_sort(lst):
    global counter
    if len(lst) == 1:
        return lst
    mid = len(lst) // 2

    counter += 2
    l1 = merge_sort(lst[:mid])
    l2 = merge_sort(lst[mid:])
    lst = merge(l1, l2)

def merge(l1, l2):
    new_lst = []
    global counter
    
    while l1 and l2:
        if l1[0] < l2[0]:
            new_lst.append(l1.pop(0))
        else:
            new_lst.append(l2.pop(0))
        counter += 1
    if l1:
        new_lst.extend(l1)
    if l2:
        new_lst.extend(l2)
    return new_lst

lo, hi, n = list(map(int, sys.argv[1:4]))
l = random.sample(range(lo, hi), n)
merge_sort(l)
print("random list of {} elements sorted with {} comparisons".format(n, counter))
print(l)
