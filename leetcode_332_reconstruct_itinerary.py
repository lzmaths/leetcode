import sys
import collections

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        m = collections.defaultdict(list)
        for source, destination in sorted(tickets, key=lambda x:x[1], reverse=True):
            m[source].append(destination)
        ans = []
        self.dfs('JFL', m, ans)
        return ans[::-1]

        
    def dfs(self, source, m, ans):
        while m[source]:
            neigh = m[source].pop()
            self.dfs(neigh, m, ans)
        ans.append(source)
