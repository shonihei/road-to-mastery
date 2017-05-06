# task: given an array of integers, find the length of longest increasing sequence

def LIS(l):
    # initialize assuming the longest sequence is 1
    arr = [1 for val in l]
    
    for i in range(1, len(l)):
        for j in range(i):
            if l[j] < l[i] and arr[j] + 1 > arr[i]:
                arr[i] += 1
    return max(arr)
