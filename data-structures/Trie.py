class TrieNode:
    ALPHABET = 26
    
    def __init__(self, is_end_of_word=False):
        self.children = [None for character in range(self.ALPHABET)]
        self.is_end = is_end_of_word
        
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def add(self, string):
        cur_node = self.root
        for c in string:
            n = cur_node.children[ord(c) - 97]
            if not n:
                cur_node.children[ord(c) - 97] = TrieNode()
            cur_node = cur_node.children[ord(c) - 97]
        cur_node.is_end = True

    def contains(self, string):
        cur_node = self.root
        for c in string:
            n = cur_node.children[ord(c) - 97]
            if not n:
                return False
            cur_node = cur_node.children[ord(c) - 97]
        if cur_node.is_end:
            return True
        else:
            return False

a = Trie()
a.add("shonihei")
a.add("shoniher")
a.add("shonihe")
a.add("shoniheiner")
print(a.contains("shonihei"))
