"""
Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 'E'
represents an unrevealed empty square, 'B' represents a revealed blank square that has no adjacent
(above, below, left, right, and all 4 diagonals) mines, digit ('1' to '8')
represents how many mines are adjacent to this revealed square, and finally 'X'
represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the board after revealing this position according to the following rules:

If a mine ('M') is revealed, then the game is over - change it to 'X'.
If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.
"""

def neighbors(board, click):
    i, j = click
    for _i in range(-1, 2):
        if _i + i < 0 or _i + i >= len(board):
            continue
        for _j in range(-1, 2):
            if _j + j < 0 or _j + j >= len(board[0]):
                continue
            if _i + i == i and _j + j == j:
                continue
            yield (_i + i, _j + j)

def updateBoard(board, click):
    i, j = click
    if board[i][j] == "M":
        board[i][j] = "X"
        return board
    else:
        bombs = 0
        for _i, _j in neighbors(board, (i, j)):
            if board[_i][_j] == "M":
                bombs += 1
        if bombs > 0:
            board[i][j] = str(bombs)
        else:
            board[i][j] = "B"
            for _i, _j in neighbors(board, (i, j)):
                if board[_i][_j] == "E":
                    updateBoard(board, [_i, _j])
        return board

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            b = [
                ['B', '1', 'E', '1', 'B'],
                ['B', '1', 'M', '1', 'B'],
                ['B', '1', '1', '1', 'B'],
                ['B', 'B', 'B', 'B', 'B']
            ]
            new_b = [
                ['B', '1', 'E', '1', 'B'],
                ['B', '1', 'X', '1', 'B'],
                ['B', '1', '1', '1', 'B'],
                ['B', 'B', 'B', 'B', 'B']
            ]
            self.assertEqual(updateBoard(b, [1, 2]), new_b)
        
        def test2(self):
            b = [
                ['E', 'E', 'E', 'E', 'E'],
                ['E', 'E', 'M', 'E', 'E'],
                ['E', 'E', 'E', 'E', 'E'],
                ['E', 'E', 'E', 'E', 'E']
            ]
            new_b = [
                ['B', '1', 'E', '1', 'B'],
                ['B', '1', 'M', '1', 'B'],
                ['B', '1', '1', '1', 'B'],
                ['B', 'B', 'B', 'B', 'B']
            ]
            self.assertEqual(updateBoard(b, [3, 0]), new_b)
    
    unittest.main()

