# task: given a string of "+" and "-", and an integer k, find the minimum number of 'flips'
#       that you need in order to make the string all "+". The size of each flip is equal
#       to k
# example:
#       - - - + - + + -    k = 3
#       + + + + - + + -    flip the first three
#       + + + + + - - -    flip the next three
#       + + + + + + + +    flip the last three
#       there are other ways to make all of them the same side up
#       but it must take 3 flips.

def flips(s, k):
    count = 0
    l = [True if c == "+" else False for c in s]
    for i in range(len(s) - (k - 1)):
        if not l[i]:
            for j in range(i, i+k):
                if l[j]:
                    l[j] = False
                else:
                    l[j] = True
            count += 1
    if all(l):
        return count
    return -1

t = int(input().strip())
for test in range(1, t+1):
    l = list(input().strip().split(' '))
    s = l[0]
    k = int(l[1])
    c = flips(s, k)
    if c < 0:
        print("Case #{}: IMPOSSIBLE".format(test))
    else:
        print("Case #{}: {}".format(test, c))
