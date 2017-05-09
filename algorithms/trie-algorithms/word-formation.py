# task: given a Trie with number of words in it, determine if a string S can be formed by concatenating two substrings in the Trie

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.end = False

def add(node, string):
    for char in string:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
    node.end = True
    
def add_words(node, lst_of_words):
    for word in lst_of_words:
        add(node, word)

def is_possible(node, string):
    i = 0
    node2 = node
    size = len(string)
    while i < size:
        if string[i] not in node.children:
            break
        node = node.children[string[i]]
        i += 1
    if not node.end:
        return False
    while i < size:
        if string[i] not in node2.children:
            return False
        node2 = node2.children[string[i]]
        i += 1
    if not node2.end:
        return False
    return True
    
words = ["geeks", "forgeeks", "quiz", "geek"]
A = TrieNode()
add_words(A, words)
