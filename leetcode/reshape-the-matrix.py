"""
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one
with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c
representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same
row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped
matrix; Otherwise, output the original matrix.
"""

def matrixReshape(nums, r, c):
    cur_r = len(nums)
    cur_c = len(nums[0])

    if r * c > cur_r * cur_c:
        return nums
    else:
        new_matrix = [[] for i in range(r)]
        column_count = 0
        current_row = 0
        for row in nums:
            for num in row:
                new_matrix[current_row].append(num)
                column_count += 1
                if column_count >= c:
                    column_count = 0
                    current_row += 1
        return new_matrix

nums = [
    [1, 2],
    [3, 4],
]
r = 1
c = 4
print(matrixReshape(nums, r, c))

r = 2
c = 4
print(matrixReshape(nums, r, c))
