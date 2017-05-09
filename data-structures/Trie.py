# task: implement a trie using a hashmap to store pointers to children

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.word_end = False

def add_string(cur_node, string):
    for c in string:
        if c not in cur_node.children:
            cur_node.children[c] = TrieNode()
        cur_node = cur_node.children[c]
    cur_node.word_end = True

def contains(cur_node, string):
    for c in string:
        if c not in cur_node.children:
            return False
        cur_node = cur_node.children[c]
    if cur_node.word_end:
        return True
    return False

def search(node, pattern):
    lst = []
    def __search(node, string, result=""):
        nonlocal lst
        if not node:
            return
        if not string and not node.word_end:
            return
        if not string and node.word_end:
            lst.append(result)
            return
        elif string[0] == "*":
            if node.word_end:
                lst.append(result)
            for k, v in node.children.items():
                __search(v, string, result + k)
        elif string[0] == "?":
            for k, v in node.children.items():
                __search(v, string[1:], result + k)
        else:
            if string[0] in node.children:
                __search(node.children[string[0]], string[1:], result + string[0])
    __search(node, pattern)
    return lst

A = TrieNode()
add_string(A, "shonihei")
add_string(A, "sho")
add_string(A, "shone")
add_string(A, "showtime")
add_string(A, "shower")
add_string(A, "shoulder")
add_string(A, "shallow")
add_string(A, "shoes")
add_string(A, "shot")
add_string(A, "shulker")
add_string(A, "bass")
add_string(A, "debaser")
add_string(A, "degrade")
add_string(A, "demonstration")
add_string(A, "!!@$%!@%^!@#!@$%")
