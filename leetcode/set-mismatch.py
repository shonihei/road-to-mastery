"""
The set S originally contains numbers from 1 to n. But unfortunately, due to the data error,
one of the numbers in the set got duplicated to another number in the set, which results in
repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to
firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.
"""

def findErrorNums(nums):
    l = [0 for i in range(len(nums))]
    for n in nums:
        l[n - 1] += 1
    out = []
    for i, n in enumerate(l):
        if n == 0:
            out += [i + 1]
        elif n == 2:
            out = [i + 1] + out
    return out
            
