# Completed
# Problem: https://leetcode.com/problems/reverse-integer/#/description

def reverseAux(x, neg, acc=0):
    if x == 0:
        if neg:
            return acc * -1
        else:
            return acc
    else:
        new_x = x // 10
        cur_digit = x % 10
        return reverseAux(new_x, neg, (acc * 10) + cur_digit)

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    neg = False
    if x < 0:
        x = x * -1
        neg = True
    return reverseAux(x, neg)

n = int(input().strip())
print(reverse(n))
