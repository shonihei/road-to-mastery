"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):
"""

def guessNumber(n):
    mid = (n + 1) // 2
    ans = guess(mid)
    if ans == 0:
        return mid
    elif ans == -1:
        return guessNumber(mid - 1)
    else:
        return guessNumber(mid + 1)
