def findDisappearedNumbers(nums):
    d = dict()
    _min = float('inf')
    _max = -1
    for num in nums:
        if num < _min:
            _min = num
        if num > _max:
            _max = num
        d[num] = True
    
    out = []
    for num in range(_min, _max + 1):
        if num not in d:
            out.append(num)
    return out

print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))