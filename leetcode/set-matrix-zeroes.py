"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
"""

def setZeroes(matrix):
	N = len(matrix)
	M = len(matrix[0])
	modded = [[False for j in range(M)] for i in range(N)]

	for i in range(N):
		for j in range(M):
			if matrix[i][j] == 0 and not modded[i][j]:
				modRow(i, M, modded, matrix)
				modCol(j, N, modded, matrix)

def modRow(row, M, modded, matrix):
	for j in range(M):
		if matrix[row][j] != 0:
			matrix[row][j] = 0
			modded[row][j] = True

def modCol(col, N, modded, matrix):
	for i in range(N):
		if matrix[i][col] != 0:
			matrix[i][col] = 0
			modded[i][col] = True
