"""
Given a List of words, return the words that can be typed using letters of alphabet on
only one row's of American keyboard like the image below.
"""

def findWords(words):
    d = {
        "q": 0,
        "w": 0,
        "e": 0,
        "r": 0,
        "t": 0,
        "y": 0,
        "u": 0,
        "i": 0,
        "o": 0,
        "p": 0,
        "a": 1,
        "s": 1,
        "d": 1,
        "f": 1,
        "g": 1,
        "h": 1,
        "j": 1,
        "k": 1,
        "l": 1,
        "z": 2,
        "x": 2,
        "c": 2,
        "v": 2,
        "b": 2,
        "n": 2,
        "m": 2,
    }
    answers = []
    for word in words:
        tmp = word.lower()
        row = d[tmp[0]]
        for char in tmp[1:]:
            if d[char] != row:
                break
        else:
            answers.append(word)
    return answers

print(findWords(["Hello", "Alaska", "Dad", "Peace"]))
