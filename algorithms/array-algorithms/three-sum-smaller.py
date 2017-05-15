# task: given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n such
#       that nums[i] + nums[j] + nums[k] < target

def naive_three_sum_smaller(nums, target):
    for i, val in enumerate(nums):
        for j, val in enumerate(nums[i+1:], i+1):
            for k, val in enumerate(nums[j+1:], j+1):
                if nums[i] + nums[j] + nums[k] < target:
                    print((i, j, k))

def three_sum_smaller(nums, target):
    res = []
    for i in range(len(nums) - 2):
        j = i + 1
        k = len(nums) - 1
        while j < k:
            print(nums[i] + nums[j] + nums[k])
            if nums[i] + nums[j] + nums[k] < target:
                res.append((i, j, k))
                j += 1
            else:
                k -= 1
    return res
