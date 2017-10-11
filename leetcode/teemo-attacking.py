"""
In LOL world, there is a hero called Teemo and his attacking can make his enemy
Ashe be in poisoned condition. Now, given the Teemo's attacking ascending time
series towards Ashe and the poisoning time duration per Teemo's attacking, you need to
output the total time that Ashe is in poisoned condition.

You may assume that Teemo attacks at the very beginning of a specific time point,
and makes Ashe be in poisoned condition immediately.
"""

def findPoisonDuration(timeSeries, duration):
    total = 0
    end = 0

    for time in timeSeries:
        if time >= end:
            total += duration
            end = time + duration
        else:
            overlap = end - time
            total += (duration - overlap)
            end += (duration - overlap)
    return total

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            self.assertEqual(findPoisonDuration([1, 4], 2), 4)

        def test2(self):
            self.assertEqual(findPoisonDuration([1, 2], 2), 3)

        def test3(self):
            self.assertEqual(findPoisonDuration([2, 4, 5], 3), 6)

    unittest.main()

