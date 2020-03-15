class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
      
        visited = [[False] * n for _ in range(m)]
        print(m, n, grid, visited)
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    self.dfs(i, j, grid, visited)
                    ans += 1

        return ans

    def dfs(self, x, y, grid, visited):
        m, n = len(grid), len(grid[0])
        visited[x][y] = True
        for dx, dy in ([-1, 0], [1, 0], [0, -1], [0, 1]):
            nx, ny = x + dx, y + dy
            #print(nx, ny, m, n, grid[nx][ny], visited )
            if nx < 0 or nx >= m or ny < 0 or ny >= n or grid[nx][ny] == '0' or visited[nx][ny]:
                continue
            self.dfs(nx, ny, grid, visited)

solution = Solution()
#grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
#print(solution.numIslands(grid))

grid = [["1"],["1"]]
print(solution.numIslands(grid))