import random

class Cell:
    def __init__(self):
        self.is_bomb = False
        self.is_revealed = False
        self.val = 0
        
    def __repr__(self):
        s = -1 if self.is_bomb else self.val
        return str(s)
        
class Minesweeper:
    def __init__(self, col_cells=10, row_cells=10, bombs=10):
        self.col_cells = col_cells
        self.row_cells = row_cells
        self.bombs = bombs
        self.grid = Minesweeper.build_grid(self.col_cells, self.row_cells, self.bombs)

    def build_grid(col_cells, row_cells, bombs):
        grid = [[Cell() for i in range(col_cells)] for j in range(row_cells)]
        bomb_cells = random.sample(range(0, col_cells * row_cells), bombs)
        for bomb in bomb_cells:
            bomb_i = bomb // row_cells
            bomb_j = bomb - (bomb_i * row_cells)
            grid[bomb_i][bomb_j].is_bomb = True

            if bomb_i - 1 >= 0:
                if bomb_j - 1 >= 0 and not grid[bomb_i - 1][bomb_j - 1].is_bomb:
                    grid[bomb_i - 1][bomb_j - 1].val += 1
                if not grid[bomb_i - 1][bomb_j].is_bomb:
                    grid[bomb_i - 1][bomb_j].val += 1
                if bomb_j + 1 < col_cells and not grid[bomb_i - 1][bomb_j + 1].is_bomb:
                    grid[bomb_i - 1][bomb_j + 1].val += 1
            if bomb_j - 1 >= 0 and not grid[bomb_i][bomb_j - 1].is_bomb:
                grid[bomb_i][bomb_j - 1].val += 1
            if bomb_j + 1 < col_cells and not grid[bomb_i][bomb_j + 1].is_bomb:
                grid[bomb_i][bomb_j + 1].val += 1
            if bomb_i + 1 < row_cells:
                if bomb_j - 1 >= 0 and not grid[bomb_i + 1][bomb_j].is_bomb:
                    grid[bomb_i + 1][bomb_j - 1].val += 1
                if not grid[bomb_i + 1][bomb_j].is_bomb:
                    grid[bomb_i + 1][bomb_j].val += 1
                if bomb_j + 1 < col_cells and not grid[bomb_i + 1][bomb_j + 1].is_bomb:
                    grid[bomb_i + 1][bomb_j + 1].val += 1
        return grid
