# task: x is in between set A and B if every element in A is a factor of x and x if a factor of every element in B.
#       given two sets, find the number of possible x values there are

def between_brute(A, B):
    count = 0
    for x in range(1, max(B) + 1):
        for a in A:
            if not x % a == 0:
                break
        else:
            for b in B:
                if not b % x == 0:
                    break
            else:
                count += 1
    return count
