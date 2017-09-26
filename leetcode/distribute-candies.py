"""
Given an integer array with even length, where different numbers in
this array represent different kinds of candies. Each number means one
candy of the corresponding kind. You need to distribute these candies
equally in number to brother and sister. Return the maximum number of kinds of
candies the sister could gain.
"""

def distributeCandies(candies):
    d = dict()
    for candy in candies:
        d[candy] = d.get(candy, 0) + 1
    
    return int(min(len(candies) / 2, len(d)))

print(distributeCandies([1, 1, 2, 3]))
print(distributeCandies([1, 1, 2, 2, 3, 3]))