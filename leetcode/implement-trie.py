"""
Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.
"""

class TrieNode(object):
	def __init__(self):
		self.end = False
		self.children = [None for i in range(26)]

class Trie(object):
	
	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.root = TrieNode()

	def insert(self, word):
		"""
		Inserts a word into the trie.
		:type word: str
		:rtype: void
		"""
		cur = self.root
		self._insert(cur, word)
	
	def _insert(self, cur, word):
		if not word:
			cur.end = True
		else:
			if not cur.children[ord(word[0]) - 97]:
				cur.children[ord(word[0]) - 97] = TrieNode()
			self._insert(cur.children[ord(word[0]) - 97], word[1:])

	def search(self, word):
		"""
		Returns if the word is in the trie.
		:type word: str
		:rtype: bool
		"""
		cur = self.root
		return self._search(cur, word)
	
	def _search(self, cur, word):
		if not word and cur.end:
			return True
		elif word:
			if not cur.children[ord(word[0]) - 97]:
				return False
			return self._search(cur.children[ord(word[0]) - 97], word[1:])
		else:
			return False

	def startsWith(self, prefix):
		"""
		Returns if there is any word in the trie that starts with the given prefix.
		:type prefix: str
		:rtype: bool
		"""
		cur = self.root
		return self._startsWith(cur, prefix)

	def _startsWith(self, cur, prefix):
		if not prefix:
			return True
		else:
			if not cur.children[ord(prefix[0]) - 97]:
				return False
			return self._startsWith(cur.children[ord(prefix[0]) - 97], prefix[1:])