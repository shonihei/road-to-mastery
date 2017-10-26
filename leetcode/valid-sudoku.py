"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
"""

def isValidSudoku(board):
    # check horizontally
    for row in board:
        d = {}
        for val in row:
            if val == ".":
                continue
            if val in d:
                return False
            else:
                d[val] = True
    
    # check vertically
    for i in range(len(board[0])):
        d = {}
        for j in range(len(board)):
            if board[j][i] == ".":
                continue
            if board[j][i] in d:
                return False
            else:
                d[board[j][i]] = True
    
    # check 3 x 3 grid
    for i in range(0, len(board), 3):
        for j in range(0, len(board[0]), 3):
            d = {}
            for k in range(3):
                for l in range(3):
                    if board[i + k][j + l] == ".":
                        continue
                    if board[i + k][j + l] in d:
                        return False
                    else:
                        d[board[i + k][j + l]] = True
    return True


if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            b = [[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]
            self.assertTrue(isValidSudoku(b))
        
        def test2(self):
            b = [[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
            self.assertFalse(isValidSudoku(b))
    
    unittest.main()