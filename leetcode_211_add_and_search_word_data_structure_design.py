import sys, collections

class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        node = self.root
        for ch in word:
            node = node.children[ch]
        node.isWord = True


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        node = self.root
        return self.searchHelper(node, word)
        
    def searchHelper(self, node, s):
        if not node:
            return False
        if not s:
            return node.isWord
        
        for ch in s:
            if ch == '.':
                for child in node.children.values():
                    if self.searchHelper(child, s[1:]):
                        return True
            else:
                return self.searchHelper(node.children.get(ch), s[1:])
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)