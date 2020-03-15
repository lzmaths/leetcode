import sys

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not words:
            return []
        ans = []
        for w in words:
            if self.findWord(board, w):
                ans.append(w)
        return ans

    def findWord(self, board, word):
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if self.dfs(i, j, board, word, visited):
                    return True
        return False
        
    def dfs(self, r, c, board, s, visited):
        if board[r][c] == s or not s:
            return True
        if board[r][c] != s[0]:
            return False
        visited[r][c] = True
        m, n = len(board), len(board[0])
        for dx, dy in ([-1, 0], [1, 0], [0, -1], [0, 1]):
            nx = r+dx
            ny = c+dy
            if nx < 0 or nx >= m or ny < 0 or ny >= n or visited[nx][ny]:
                continue
            if self.dfs(nx, ny, board, s[1:], visited):
                return True

        visited[r][c] = False
        return False


#### Above solution is LTE (limited time exceed), so we have to use a different way: Trie
import collections

class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False
    
class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True
    
    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isWord

class SolutionTrie(object):
    def findWords(self, board, words):
        ans = []
        trie = Trie()
        for w in words:
            trie.insert(w)

        m, n = len(board), len(board[0])
        
        for i in range(m):
            for j in range(n):
                visited = [[False] * n for _ in range(m)]
                self.dfs(i, j, board, trie.root, "", ans, visited)

        return ans

    def dfs(self, i, j, board, node, path, ans, visited):
        if node.isWord:
            ans.append(path)
            node.isWord = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j]:
            return 

        node = node.children.get(board[i][j])
        if not node:
            return
        visited[i][j] = True
        for dx, dy in ([-1, 0], [1, 0], [0, -1], [0, 1]):
            nx = i+dx
            ny = j+dy
            self.dfs(nx, ny, board, node, path + board[i][j], ans, visited)
        visited[i][j] = False
        