"""
You're now a baseball game point recorder.

Given a list of strings, each string can be one of the 4 following types:

Integer (one round's score): Directly represents the number of points you get in this round.
"+" (one round's score): Represents that the points you get in this round are the sum of the
last two valid round's points.
"D" (one round's score): Represents that the points you get in this round are the doubled data
of the last valid round's points.
"C" (an operation, which isn't a round's score): Represents the last valid round's points you
get were invalid and should be removed.
Each round's operation is permanent and could have an impact on the round before and the round after.

You need to return the sum of the points you could get in all the rounds.
"""

def calPoints(ops):
    stack = []
    for op in ops:
        if op == "+":
            score = stack[-1] + stack[-2]
            stack.append(score)
        elif op == "D":
            score = stack[-1] * 2
            stack.append(score)
        elif op == "C":
            stack.pop()
        else:
            stack.append(int(op))
    return sum(stack)

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            self.assertEqual(calPoints(["5","2","C","D","+"]), 30)
        
        def test2(self):
            self.assertEqual(calPoints(["5","-2","4","C","D","9","+","+"]), 27)

    unittest.main()
