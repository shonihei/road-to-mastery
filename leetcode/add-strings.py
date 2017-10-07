"""
Given two non-negative integers num1 and num2 represented as string,
return the sum of num1 and num2.
"""

def addStrings(num1, num2):
    d = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
    }
    
    mult = 1
    total = 0

    for i in range(len(num1) - 1, -1, -1):
        total += d[num1[i]] * mult
        mult *= 10
    
    mult = 1
    for i in range(len(num2) - 1, -1, -1):
        total += d[num2[i]] * mult
        mult *= 10

    return str(total)


if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            self.assertEqual(addStrings("23", "49"), "72")

    unittest.main()
    