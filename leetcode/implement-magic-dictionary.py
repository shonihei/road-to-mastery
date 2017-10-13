"""
Implement a magic directory with buildDict, and search methods.

For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.

For the method search, you'll be given a word, and judge whether if you modify exactly one character into
another character in this word, the modified word is in the dictionary you just built.
"""

class MagicDictionary(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.wordsdic={}

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for i in dict:
            self.wordsdic[len(i)]=self.wordsdic.get(len(i),[])+[i]

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for candi in self.wordsdic.get(len(word),[]):
            countdiff=0
            for j in range(len(word)):
                if candi[j]!=word[j]:
                    countdiff+=1
            if countdiff==1:
                return True
        return False

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            a = MagicDictionary()
            a.buildDict(["hello", "leetcode"])
            self.assertTrue(a.search("hhllo"))
    
    unittest.main()