"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""

def spiralOrder(matrix):
	if not matrix or not matrix[0]:
		return []
	out = []
	visited = [[False for i in range(len(matrix[j]))] for j in range(len(matrix))]
	i = j = 0
	direction = [0, 1]
	while True:
		out.append(matrix[i][j])
		visited[i][j] = True
		new_i, new_j = i + direction[0], j + direction[1]
		if 0 <= new_i < len(matrix) and 0 <= new_j < len(matrix[new_i]) and not visited[new_i][new_j]:
			i, j = new_i, new_j
		else:
			next_found = False
			if j + 1 < len(matrix[0]) and visited[i][j + 1] == 0:
				next_found = True
				direction = [0, 1]
				j += 1
			elif i + 1 < len(matrix) and visited[i + 1][j] == 0:
				next_found = True
				direction = [1, 0]
				i += 1
			elif j - 1 >= 0 and visited[i][j - 1] == 0:
				next_found = True
				direction = [0, -1]
				j -= 1
			elif i - 1 >= 0 and visited[i - 1][j] == 0:
				next_found = True
				direction = [-1, 0]
				i -= 1
			if not next_found:
				return out

