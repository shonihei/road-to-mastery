"""
In English, we have a concept called root, which can be followed by some other words to form another longer word -
let's call this word successor. For example, the root an, followed by other, which can form another word another.

Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence
with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.

You need to output the sentence after the replacement.
"""

def replaceWords(roots, sentence):
    rootset = set(roots)

    def replace(word):
        for i in range(1, len(word)):
            if word[:i] in rootset:
                return word[:i]
        return word

    return " ".join(map(replace, sentence.split()))

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            d = ["cat", "bat", "rat"]
            s = "the cattle was rattled by the battery"
            o = "the cat was rat by the bat"
            self.assertEqual(replaceWords(d, s), o)

    unittest.main()
