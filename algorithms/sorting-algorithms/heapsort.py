# task: implement a heapsort algorithm

def heap_sort(l):
    heapify(l)
    e = len(l) - 1
    while e > 0:
        l[0], l[e] = l[e], l[0]
        e -= 1
        siftdown(l, 0, e)

def heapify(l):
    e = len(l) - 1
    s = (len(l) - 2) // 2
    while s >= 0:
        siftdown(l, s, e)
        s -= 1

def siftdown(l, s, e):
    while (s * 2 + 1) <= e:
        lc = s * 2 + 1
        if lc + 1 <= e and l[lc + 1] > l[lc]:
            lc += 1
        if l[lc] > l[s]:
            l[lc], l[s] = l[s], l[lc]
            s = lc
        else:
            break
