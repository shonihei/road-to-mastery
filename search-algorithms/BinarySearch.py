def search(target, lst):
    if not lst:
        return False
    elif len(lst) == 1:
        return lst[0] == target
    m = len(lst) // 2
    if target == lst[m]:
        return True
    elif target < lst[m]:
        return search(target, lst[:m])
    else:
        return search(target, lst[m+1:])

def main():
    lst = [1, 4, 5, 8, 12, 13, 15, 18]
    print(search(5, lst))
    print(search(10, lst))
    print(search(100, []))

if __name__ == "__main__":
    main()
