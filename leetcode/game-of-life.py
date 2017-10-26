"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.
"""

def gameOfLife(board):
    ref = [[state for state in board[i]] for i in range(len(board))]
    for i in range(len(ref)):
        for j in range(len(ref[0])):
            num_live_neighbors = live_neighbors(ref, i, j)
            if ref[i][j] == 1:
                if num_live_neighbors < 2 and num_live_neighbors > 3:
                    board[i][j] = 0
            else:
                if num_live_neighbors == 3:
                    board[i][j] = 1
    
                

def live_neighbors(board, i, j):
    live_cells = 0
    for k in range(-1, 2):
        if i + k < 0 or i + k >= len(board):
            continue
        for l in range(-1, 2):
            if j + l < 0 or j + l >= len(board[0]):
                continue
            if k == 0 and l == 0:
                continue
            if board[i + k][j + l] == 1:
                live_cells += 1
    return live_cells
