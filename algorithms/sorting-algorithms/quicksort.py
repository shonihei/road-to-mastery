def quick_sort(lst):
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
                lo += 1
                if lo > hi:
                    done = True
                    break
            if done:
                break
            while lst[hi] > lst[pivot]:
                hi -= 1
                if hi < lo:
                    done = True
                    break
            if done:
                break
            lst[lo], lst[hi] = lst[hi], lst[lo]
        lst[lo], lst[pivot] = lst[pivot], lst[lo]
        pivot = lo
        return quick_sort(lst[:pivot]) + [lst[pivot]] + quick_sort(lst[pivot + 1:])

def main():
    import sys
    import random
    SIZE = int(sys.argv[1])
    LO = int(sys.argv[2])
    HI = int(sys.argv[3])
    l = random.sample(range(LO, HI), SIZE)
    print("original list: \t{}".format(l))
    sorted_l = quick_sort(l)
    print("sorted list: \t{}".format(sorted_l))
    l.sort()
    print("cor answer: \t{}".format(l))
    if sorted_l == l:
        print("Correct!")
    else:
        print("Incorrect...")
    
if __name__ == "__main__":
    main()
