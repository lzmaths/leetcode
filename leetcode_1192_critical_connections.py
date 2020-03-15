import sys, collections

class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]

        The idea is to check if there is cycle, (by checking if the level get changed)
        """
        g = collections.defaultdict(set)
        for u, v in connections:
            g[u].add(v)
            g[v].add(u)
        
        path = [-1] * n
        
        res = []
        self.dfs(0, -1, 0, path, res, g)
        return res
        
    def dfs(self, curr, parent, level, path, res, g):
        path[curr]= level + 1
        for child in g[curr]:
            #print("child", curr, child, path)
            if child == parent:
                continue
            elif path[child] == -1:
                path[curr] = min(path[curr], self.dfs(child, curr, level+1, path, res, g))
            else:
                path[curr] = min(path[curr], path[child])
        #print(curr, path, path[curr], level)
        # we don't want to add [-1, 0], so add curr != 0
        if path[curr] == level + 1 and curr != 0:
            res.append([parent, curr])
                
        
        return path[curr]


solution = Solution()
n = 4
connections = [[0,1],[1,2],[2,0],[1,3]]
print(solution.criticalConnections(n, connections))