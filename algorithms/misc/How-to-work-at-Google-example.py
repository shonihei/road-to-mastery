# Completed
# Problem: https://www.youtube.com/watch?v=XKu_SEDAykw&index=11&list=WL&ab_channel=LifeatGoogle

def hasPairWithSumSorted(lst, target):
    lo = 0
    hi = len(lst) - 1
    while lo < hi:
        s = lst[lo] + lst[hi]
        if s == target:
            return True
        elif s < target:
            lo += 1
        else:
            hi -= 1
    return False

def hasPairWithSumUnsorted(lst, target):
    d = {}
    for n in lst:
        counterPart = target - n
        if counterPart in d:
            return True
        d[n] = True
    return False

def main():
    lst = [1, 2, 3, 4, 6, 7]
    print("hasPairWithSumSorted:")
    print(hasPairWithSumSorted(lst, 10))
    print(hasPairWithSumSorted(lst, 20))
    print('')

    print("hasPairWithSumUnsorted:")
    print(hasPairWithSumUnsorted([28, 21, 3, 4, 6, 8, 19], 27))
    print(hasPairWithSumUnsorted([3, 4, 56, 21, 2, 4, 65], 100))
    print(hasPairWithSumUnsorted([10, 12, 12, 10], 20))
if __name__ == "__main__":
    main()
