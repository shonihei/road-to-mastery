# task: given an array with negative and positive numbers, find a subarray such that its sum is maximized

# simple solution that does not keep track of the start and end indices
def maximum_subarray_simple(lst):
    cur_max = 0
    global_max = -float("inf")
    for val in lst:
        cur_max += val
        if cur_max <= 0:
            cur_max = 0
        elif cur_max > global_max:
            global_max = cur_max
    return global_max

# O(n) time complexity with O(1) space complexity
# if the maximum sum is negative then return 0 since not picking any element
# maximizes the sum
def maximum_subarray(lst):
    cur_start = 0
    max_start = 0
    max_end = 0

    global_max = -float('inf')
    cur_max = 0
    for i, val in enumerate(lst):
        cur_max += val
        if cur_max > global_max:
            global_max = cur_max
            max_start = cur_start
            max_end = i
        if cur_max <= 0:
            cur_start = i + 1
            cur_max = 0
    if global_max < 0:
        return 0, None, None
    return global_max, max_start, max_end
