"""
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s
elements are subset of nums2. Find all the next greater numbers for nums1's
elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number
to its right in nums2. If it does not exist, output -1 for this number.
"""

def nextGreaterElement(findNums, nums):
    d = dict()
    for i, n in enumerate(nums):
        d[n] = i

    out = []
    for n in findNums:
        i = d[n] + 1
        while i < len(nums):
            if nums[i] > n:
                out.append(nums[i])
                break
            i += 1
        else:
            out.append(-1)
    return out

print(nextGreaterElement([4,1,2], [1, 3, 4, 2]))
