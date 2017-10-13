"""
map is defined as a 2D matrix of integers. If adjacent elements have the same number, it is considered part of the same country.
Even if 2 elements have the same integer, if they are not adjacent to each other horizontally or vertically then they are
considered two separate countries.

write a function countCountries that takes a map and returns how many countries there are.
"""

def countCountries(map):
    out = 0
    visited = [[False for i in range(len(map[0]))] for j in range(len(map))]
    
    for i in range(len(map)):
        for j in range(len(map[0])):
            visited[i][j] = True
            if i - 1 >= 0 and map[i - 1][j] == map[i][j]:
                if not visited[i - 1][j]:
                    visited[i - 1][j] == True
                continue
            if j - 1 >= 0 and map[i][j - 1] == map[i][j] and visited[i][j - 1] is True:
                continue
            if i + 1 < len(map) and map[i + 1][j] == map[i][j] and visited[i + 1][j] is True:
                continue
            if j + 1 < len(map[0]) and map[i][j + 1] == map[i][j] and visited[i][j + 1] is True:
                continue
            out += 1
    return out

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            _map = [
                [1, 2, 2, 2, 2],
                [1, 3, 1, 4, 2],
                [1, 3, 1, 5, 2],
                [1, 3, 2, 2, 2]
            ]
            self.assertEqual(countCountries(_map), 6)

    unittest.main()
