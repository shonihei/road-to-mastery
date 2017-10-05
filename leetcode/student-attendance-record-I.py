"""
You are given a string representing an attendance record for
a student. The record only contains the following three characters:

'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain
more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to
his attendance record.
"""

def checkRecord(s):
    absent = False
    late = 0
    for c in s:
        if c == "A":
            if absent:
                return False
            if late > 0:
                late = 0
            absent = True
        if c == "L":
            late += 1
            if late > 2:
                return False
        else:
            late = 0
    return True

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            self.assertTrue(checkRecord("PPALLP"))
        
        def test2(self):
            self.assertFalse(checkRecord("PPALLL"))

    unittest.main()