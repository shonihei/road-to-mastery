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
        sc = s * 2 + 1
        if sc + 1 <= e and l[sc + 1] > l[sc]:
            sc += 1
        if l[sc] > l[s]:
            l[sc], l[s] = l[s], l[sc]
        s = sc
