import sys, random, pprint
pp = pprint.PrettyPrinter(indent=2)

def radix_sort(lst):
    global debug
    bins = [[] for i in range(10)]
    digit = 10
    max_num = max(lst) * 10
    while digit < max_num:
        for item in lst:
            bins[(item % digit) // (digit // 10)].append(item)
        lst.clear()

        # for debugging purposes
        if debug:
            print("{}'s digit buckets:".format(digit // 10))
            pp.pprint(bins)
            print('')

        for _bin in bins:
            for i in _bin:
                lst.append(i)
            _bin.clear()
        digit *= 10
    return lst

debug = True
lo, hi, n = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
l = random.sample(range(lo, hi), n)
l = radix_sort(l)
print("random list of {} elements was sorted!".format(n))
print(l)
