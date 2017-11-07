"""
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

def generateMatrix(n):
	matrix = [[0 for i in range(n)] for j in range(n)]
	i = j = 0
	n = 1
	direction = [0, 1]
	while True:
		matrix[i][j] = n
		n += 1
		new_i = i + direction[0]
		new_j = j + direction[1]
		if 0 <= new_i < len(matrix) and 0 <= new_j < len(matrix[0]) and matrix[new_i][new_j] == 0:
			i += direction[0]
			j += direction[1]
		else:
			next_found = False
			if j + 1 < len(matrix[0]) and matrix[i][j + 1] == 0:
				next_found = True
				direction = [0, 1]
				j += 1
			elif i + 1 < len(matrix) and matrix[i + 1][j] == 0:
				next_found = True
				direction = [1, 0]
				i += 1
			elif j - 1 >= 0 and matrix[i][j - 1] == 0:
				next_found = True
				direction = [0, -1]
				j -= 1
			elif i - 1 >= 0 and matrix[i - 1][j] == 0:
				next_found = True
				direction = [-1, 0]
				i -= 1
			if not next_found:
				return matrix