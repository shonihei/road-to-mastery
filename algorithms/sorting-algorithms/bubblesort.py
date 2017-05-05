# task: implement a bubble sort

def bubble_sort(l):
    for i in range(len(l) - 1, 0, -1):
        for j in range(0, i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]

