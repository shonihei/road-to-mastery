"""
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix
in diagonal order as shown in the below image.
"""

def findDiagonalOrder(matrix):
    i = 0
    j = 0
    out = []
    N = len(matrix)
    M = len(matrix[0])
    while i != N - 1 and j != M - 1:
        out.append(matrix[i][j])
        if i - 1 < 0:
            j -= 0
        
