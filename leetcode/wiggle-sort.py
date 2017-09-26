def wiggleSort(nums):
    for i in range(1, len(nums) - 1):
        left = nums[i - 1]
        right = nums[i + 1]
        if i % 2 == 0:
            if left >= nums[i]:
                swap(nums, i, i-1)
        else:
            if left <= nums[i]:
                swap(nums, i, i+1)
    return nums

def swap(lst, a, b):
    tmpa = lst[a]
    tmpb = lst[b]
    lst[a] = tmpb
    lst[b] = tmpa
    return lst

print(wiggleSort([3, 5, 2, 1, 6, 4]))