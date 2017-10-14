"""
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. 
For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C.
And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class.
If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not.
And you have to output the total number of friend circles among all the students.
"""

def findCircleNum(M):
    visited = [False for i in range(len(M))]

    count = 0
    for i in range(len(M)):
        if not visited[i]:
            count += 1
            visit_all(M, visited, i)
    return count

def visit_all(M, visited, i):
    visited[i] = True

    for j in range(len(M)):
        if M[i][j] == 1 and not visited[j]:
            visit_all(M, visited, j)

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            a = [
                [1,1,0],
                [1,1,0],
                [0,0,1]
            ]
            self.assertEqual(findCircleNum(a), 2)

        def test2(self):
            a = [
                [1, 0, 1, 0, 0, 0],
                [0, 1, 0, 1, 0, 0],
                [1, 0, 1, 1, 0, 0],
                [0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 1, 1],
                [0, 0, 0, 0, 1, 1]
            ]
            self.assertEqual(findCircleNum(a), 2)
    
    unittest.main()
