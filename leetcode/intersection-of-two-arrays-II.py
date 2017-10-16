"""
Given two arrays, write a function to compute their intersection.
"""

def intersect(nums1, nums2):
    d = {}
    for n in nums1:
        d[n] = d.get(n, 0) + 1
    out = []
    for n in nums2:
        if n in d and d[n] > 0:
            out.append(n)
            d[n] -= 1
    return out
