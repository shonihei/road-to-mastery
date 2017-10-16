"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.
"""

def isPerfectSquare(num):
    if num <= 0:
        return False
    base = 1
    increment = 3
    while base < num:
        base += increment
        increment += 2
    return base == num
