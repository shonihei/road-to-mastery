# Given two integers x and y, calculate the Hamming distance.

def hammingDistance(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    z = x ^ y
    z = bin(z)[2:]

    total = 0
    for c in z:
        if c == "1":
            total += 1
    return total

print(hammingDistance(1, 4))