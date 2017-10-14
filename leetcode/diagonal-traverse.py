"""
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.
"""

def findDiagonalOrder(matrix):
    if len(matrix) == 0:
        return []
    i = j = 0
    up = True
    out = []
    while True:
        out.append(matrix[i][j])
        if i == len(matrix) - 1 and j == len(matrix[0]) - 1:
            return out
        if up:
            if i - 1 < 0:
                if j + 1 == len(matrix[0]):
                    i += 1
                else:
                    j += 1
                up = False
            elif j + 1 == len(matrix[0]):
                i += 1
                up = False
            else:
                i -= 1
                j += 1
        else:
            if i + 1 == len(matrix):
                j += 1
                up = True
            elif j - 1 < 0:
                if i + 1 == len(matrix):
                    j += 1
                else:
                    i += 1
                up = True
            else:
                i += 1
                j -= 1

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            a = [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ]
            b = [1, 2, 4, 7, 5, 3, 6, 8, 9]
            self.assertEqual(findDiagonalOrder(a), b)
        
        def test2(self):
            a = [[1]]
            self.assertEqual(findDiagonalOrder(a), [1])
    
        def test3(self):
            a = [[1], [2], [3]]
            self.assertEqual(findDiagonalOrder(a), [1, 2, 3])
        
        def test4(self):
            self.assertEqual(findDiagonalOrder([]), [])
        
        def test5(self):
            self.assertEqual(findDiagonalOrder([[2, 5, 8], [4, 0, -1]]), [2, 5, 4, 0, 8, -1])

    unittest.main()
