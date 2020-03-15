import sys

class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        n = len(S)
        if n == 0:
            return []
        left = self.distance(S, C)
        right = self.distance(S[::-1], C)[::-1]
        
        for i in range(n):
            left[i] = min(left[i], right[i])
        return left
        
    def distance(self, s, c):
        n = len(s)
        ans = [sys.maxsize] * n
        idx = s.find(c)
        curr = idx
        for i in range(idx, n):
            if s[i] == c:
                curr = i
            ans[i] = i - curr
                
        return ans