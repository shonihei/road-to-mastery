def merge_sort(lst):
    if len(lst) == 1:
        return lst
    mid = len(lst) // 2

    l1 = merge_sort(lst[:mid])
    l2 = merge_sort(lst[mid:])

    return merge(l1, l2)

def merge(l1, l2):
    new_lst = []
    while l1 and l2:
        if l1[0] < l2[0]:
            new_lst.append(l1.pop(0))
        else:
            new_lst.append(l2.pop(0))
    if l1:
        new_lst.extend(l1)
    if l2:
        new_lst.extend(l2)
    return new_lst

def main():
    import sys
    import random
    SIZE = int(sys.argv[1])
    LO = int(sys.argv[2])
    HI = int(sys.argv[3])
    l = random.sample(range(LO, HI), SIZE)
    print("original list: \t{}".format(l))
    sorted_l = merge_sort(l)
    print("sorted list: \t{}".format(sorted_l))
    l.sort()
    print("cor answer: \t{}".format(l))
    if sorted_l == l:
        print("Correct!")
    else:
        print("Incorrect...")

if __name__ == "__main__":
    main()
