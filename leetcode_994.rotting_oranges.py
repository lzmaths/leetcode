import sys, collections

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
        ans = 0
        q = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append([i, j, 0])
        ans = 0
        while q:
            k = len(q)
            #print(k, q)
            visited = set()
            for _ in range(k):
                rx, ry, ans = q.popleft()
                for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    nx, ny = rx + dx, ry + dy
                    if nx < 0 or nx >= m or ny < 0 or ny >= n or grid[nx][ny] != 1 or (nx, ny) in visited:
                        continue
                    #print(nx, ny, grid[nx][ny])
                    visited.add((nx, ny))
                    grid[nx][ny] = 2
                    q.append([nx, ny, ans+1])
            
        if any(1 in row for row in grid):
            return -1
        return ans