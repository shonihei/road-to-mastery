"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
"""

def letterCombinations(digits):
    if not digits:
        return []

    digit_to_letters = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    choices = []
    for digit in digits:
        choices.append(digit_to_letters[digit])
    
    output = []
    backtrack(choices, output, "")
    return output

def backtrack(choices, output, chosen):
    if not choices:
        output.append(chosen)
    else:
        cur_choices = choices[0]
        for i in range(len(cur_choices)):
            choice = cur_choices[i]
            backtrack(choices[1:], output, chosen + choice)

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            out = ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
            self.assertEqual(letterCombinations("23"), out)
        
        def test2(self):
            out = []
            self.assertEqual(letterCombinations(""), [])
    
    unittest.main()