"""
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
"""

def sortColors(nums):
    colors = [0, 0, 0]
    for num in nums:
        colors[num] += 1
    k = 0
    for i in range(len(colors)):
        for j in range(colors[i]):
            nums[k] = i
            k += 1
    
