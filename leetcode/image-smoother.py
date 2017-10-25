"""
Given a 2D integer matrix M representing the gray scale of an image, you need to design a
smoother to make the gray scale of each cell becomes the average gray scale (rounding down)
of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then
use as many as you can.
"""

def imageSmoother(M):
    N = [[0 for i in range(len(M[0]))] for j in range(len(M))]
    for i in range(len(M)):
        for j in range(len(M[0])):
            counter = 1
            _sum = M[i][j]
            if j - 1 >= 0:
                counter += 1
                _sum += M[i][j - 1]
            if j + 1 < len(M[0]):
                counter += 1
                _sum += M[i][j + 1]
            if i - 1 >= 0:
                counter += 1
                _sum += M[i - 1][j]
                if j - 1 >= 0:
                    counter += 1
                    _sum += M[i - 1][j - 1]
                if j + 1 < len(M[0]):
                    counter += 1
                    _sum += M[i - 1][j + 1]
            if i + 1 < len(M):
                counter += 1
                _sum += M[i + 1][j]
                if j - 1 >= 0:
                    counter += 1
                    _sum += M[i + 1][j - 1]
                if j + 1 < len(M[0]):
                    counter += 1
                    _sum += M[i + 1][j + 1]
            N[i][j] = _sum // counter
    return N

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            grid = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
            ans = [[4,4,5],[5,6,6],[8,9,9],[11,12,12],[13,13,14]]
            self.assertEqual(imageSmoother(grid), ans)
    
    unittest.main()
